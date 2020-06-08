# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015 Rossen Georgiev <rossen@rgp.io>
Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import asyncio
import json
import re
import struct
from base64 import b64decode
from operator import attrgetter
from os import urandom as random_bytes
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    Iterable,
    Optional,
    Tuple,
    Union
)

import aiohttp
from Cryptodome.Cipher import AES as AES, PKCS1_OAEP
from Cryptodome.Hash import HMAC, SHA1
from Cryptodome.PublicKey.RSA import import_key as rsa_import_key

from .enums import EInstanceFlag, EType, ETypeChar, EUniverse

__all__ = (
    'get',
    'find',
    'make_steam64',
    'parse_trade_url_token',
)

BS = 16
PROTOBUF_MASK = 0x80000000
MAX_ASYNCIO_SECONDS = 3456000
_INVITE_HEX = '0123456789abcdef'
_INVITE_CUSTOM = 'bcdfghjkmnpqrtvw'
_INVITE_VALID = f'{_INVITE_HEX}{_INVITE_CUSTOM}'
_INVITE_MAPPING = dict(zip(_INVITE_HEX, _INVITE_CUSTOM))
_INVITE_INVERSE_MAPPING = dict(zip(_INVITE_CUSTOM, _INVITE_HEX))


# from ValvePython/steam

ETypeChars = ''.join(type_char.name for type_char in ETypeChar)


class UniverseKey:
    Public = rsa_import_key(b64decode("""
MIGdMA0GCSqGSIb3DQEBAQUAA4GLADCBhwKBgQDf7BrWLBBmLBc1OhSwfFkRf53T
2Ct64+AVzRkeRuh7h3SiGEYxqQMUeYKO6UWiSRKpI2hzic9pobFhRr3Bvr/WARvY
gdTckPv+T1JzZsuVcNfFjrocejN1oWI0Rrtgt4Bo+hOneoo3S57G9F1fOpn5nsQ6
6WOiu4gZKODnFMBCiQIBEQ==
"""))


def pad(s):
    return s + (BS - len(s) % BS) * struct.pack('B', BS - len(s) % BS)


def unpad(s):
    return s[0:-s[-1]]


def generate_session_key(hmac_secret=b''):
    session_key = random_bytes(32)
    encrypted_session_key = PKCS1_OAEP.new(UniverseKey.Public, SHA1).encrypt(session_key + hmac_secret)

    return session_key, encrypted_session_key


def symmetric_encrypt(message, key):
    iv = random_bytes(BS)
    return symmetric_encrypt_with_iv(message, key, iv)


def symmetric_encrypt_HMAC(message, key, hmac_secret):
    prefix = random_bytes(3)
    hmac = hmac_sha1(hmac_secret, prefix + message)
    iv = hmac[:13] + prefix
    return symmetric_encrypt_with_iv(message, key, iv)


def symmetric_encrypt_iv(iv, key):
    return AES.new(key, AES.MODE_ECB).encrypt(iv)


def symmetric_encrypt_with_iv(message, key, iv):
    encrypted_iv = symmetric_encrypt_iv(iv, key)
    cyphertext = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(message))
    return encrypted_iv + cyphertext


def symmetric_decrypt(cyphertext, key):
    iv = symmetric_decrypt_iv(cyphertext, key)
    return symmetric_decrypt_with_iv(cyphertext, key, iv)


def symmetric_decrypt_HMAC(cyphertext, key, hmac_secret):
    iv = symmetric_decrypt_iv(cyphertext, key)
    message = symmetric_decrypt_with_iv(cyphertext, key, iv)

    hmac = hmac_sha1(hmac_secret, iv[-3:] + message)

    if iv[:13] != hmac[:13]:
        raise RuntimeError("Unable to decrypt message. HMAC does not match.")

    return message


def symmetric_decrypt_iv(cyphertext, key):
    return AES.new(key, AES.MODE_ECB).decrypt(cyphertext[:BS])


def symmetric_decrypt_with_iv(cyphertext, key, iv):
    return unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(cyphertext[BS:]))


def hmac_sha1(secret, data):
    return HMAC.new(secret, data, SHA1).digest()


def is_proto(emsg: bytes) -> bool:
    return (int(emsg) & PROTOBUF_MASK) > 0


def set_proto_bit(emsg: int) -> int:
    return int(emsg) | PROTOBUF_MASK


def clear_proto_bit(emsg: bytes) -> int:
    return int(emsg) & ~PROTOBUF_MASK


def make_steam64(id: int = 0, *args, **kwargs) -> int:
    """Returns a Steam 64-bit ID from various other representations.

    .. code:: python

        make_steam64()  # invalid steam_id
        make_steam64(12345)  # account_id
        make_steam64('12345')
        make_steam64(id=12345, type='Invalid', universe='Invalid', instance=0)
        make_steam64(103582791429521412)  # steam64
        make_steam64('103582791429521412')
        make_steam64('STEAM_1:0:2')  # steam2
        make_steam64('[g:1:4]')  # steam3
        make_steam64('cv-dgb')  # invite code

    Raises
    ------
    :exc:`TypeError`
        Too many arguments have been given.

    Returns
    -------
    :class:`int`
        The 64-bit Steam ID.
    """

    etype = EType.Invalid
    universe = EUniverse.Invalid
    instance = None

    if len(args) == 0 and len(kwargs) == 0:
        value = str(id)

        # numeric input
        if value.isdigit():
            value = int(value)

            # 32 bit account id
            if 0 < value < 2 ** 32:
                id = value
                etype = EType.Individual
                universe = EUniverse.Public
            # 64 bit
            elif value < 2 ** 64:
                return value
            else:
                id = 0

        # textual input e.g. [g:1:4]
        else:
            result = steam2_to_tuple(value) or steam3_to_tuple(value) or invite_code_to_tuple(value)

            if result:
                id, etype, universe, instance = result
            else:
                id = 0

    elif len(args) > 0:
        length = len(args)
        if length == 1:
            etype = args
        elif length == 2:
            etype, universe = args
        elif length == 3:
            etype, universe, instance = args
        else:
            raise TypeError(f"Takes at most 4 arguments ({length} given)")

    if len(kwargs) > 0:
        etype = kwargs.get('type', etype)
        universe = kwargs.get('universe', universe)
        instance = kwargs.get('instance', instance)

    etype = EType.try_value(etype)
    universe = EUniverse.try_value(universe)

    if instance is None:
        instance = 1 if etype in (EType.Individual, EType.GameServer) else 0

    return (universe.value << 56) | (etype.value << 52) | (instance << 32) | id


def steam2_to_tuple(value: str) -> Optional[Tuple[int, EType, EUniverse, int]]:
    """
    Parameters
    ----------
    value: :class:`str`
        steam2 e.g. ``STEAM_1:0:1234``.

    Returns
    -------
    Optional[:class:`tuple`]
        e.g. (account_id, type, universe, instance) or ``None``.

    .. note::
        The universe will be always set to ``1``. See :attr:`SteamID.as_steam2`.
    """
    match = re.match(
        r"^STEAM_(?P<universe>\d+)"
        r":(?P<reminder>[0-1])"
        r":(?P<id>\d+)$", value
    )

    if not match:
        return None

    steam_32 = (int(match.group('id')) << 1) | int(match.group('reminder'))
    universe = int(match.group('universe'))

    # games before orange box used to incorrectly display universe as 0, we support that
    if universe == 0:
        universe = 1

    return steam_32, EType(1), EUniverse(universe), 1


def steam3_to_tuple(value: str) -> Optional[Tuple[int, EType, EUniverse, int]]:
    """
    Parameters
    ----------
    value: :class:`str`
        steam3 e.g. ``[U:1:1234]``.

    Returns
    -------
    Optional[:class:`tuple`]
        e.g. (account_id, type, universe, instance) or ``None``.
    """
    match = re.match(
        rf"^\[(?P<type>[i{ETypeChars}]):"  # type char
        r"(?P<universe>[0-4]):"  # universe
        r"(?P<id>\d{1,10})"  # accountid
        r"(:(?P<instance>\d+))?\]$",  # instance
        value
    )
    if not match:
        return None

    steam_32 = int(match.group('id'))
    universe = EUniverse(int(match.group('universe')))
    typechar = match.group('type').replace('i', 'I')
    etype = EType(ETypeChar[typechar])
    instance = match.group('instance')

    if typechar in 'gT':
        instance = 0
    elif instance is not None:
        instance = int(instance)
    elif typechar == 'L':
        instance = EInstanceFlag.Lobby
    elif typechar == 'c':
        instance = EInstanceFlag.Clan
    elif etype in (EType.Individual, EType.GameServer):
        instance = 1
    else:
        instance = 0

    instance = int(instance)

    return steam_32, etype, universe, instance


def invite_code_to_tuple(code: str) -> Optional[Tuple[int, EType, EUniverse, int]]:
    """
    Parameters
    ----------
    code: :class:`str`
        The invite code e.g. ``cv-dgb``

    Returns
    -------
    Optional[:class:`tuple`]
        e.g. (account_id, type, universe, instance) or ``None``.
    """
    match = re.match(rf'(https?://s\.team/p/(?P<code1>[\-{_INVITE_VALID}]+))'
                     rf'|(?P<code2>[\-{_INVITE_VALID}]+$)', code)
    if not match:
        return None

    code = (match.group('code1') or match.group('code2')).replace('-', '')

    def repl_mapper(x):
        return _INVITE_INVERSE_MAPPING[x.group()]

    steam_32 = int(re.sub(f"[{_INVITE_CUSTOM}]", repl_mapper, code), 16)

    if 0 < steam_32 < 2 ** 32:
        return steam_32, EType(1), EUniverse.Public, 1


async def steam64_from_url(url: str, timeout: float = 30) -> Optional[int]:
    """Takes a Steam Community url and returns steam64 or None

    .. note::
        Each call makes a http request to steamcommunity.com

    .. note::
        Example URLs
            https://steamcommunity.com/gid/[g:1:4]

            https://steamcommunity.com/gid/103582791429521412

            https://steamcommunity.com/groups/Valve

            https://steamcommunity.com/profiles/[U:1:12]

            https://steamcommunity.com/profiles/76561197960265740

            https://steamcommunity.com/id/johnc

    Parameters
    ----------
    url: :class:`str`
        The Steam community url.
    timeout: :class:`int`
        How long to wait on http request before turning ``None``.

    Returns
    -------
    steam64: Optional[:class:`int`]
        If ``steamcommunity.com`` is down or no matching account is found returns ``None``
    """

    search = re.search(r'^(?P<clean_url>(?:http[s]?://|)(?:www\.|)steamcommunity\.com/'
                       r'(?P<type>profiles|id|gid|groups)/(?P<value>.*?))(?:/(?:.*)?)?$',
                       str(url), flags=re.M)

    if search is None:
        return None

    session = aiohttp.ClientSession()

    # user profiles
    try:
        if search.group('type') in ('id', 'profiles'):
            r = await session.get(search.group('clean_url'), timeout=timeout)
            text = await r.text()
            data_match = re.search("g_rgProfileData\s*=\s*(?P<json>{.*?});\s*", text)

            if data_match:
                data = json.loads(data_match.group('json'))
                return int(data['steamid'])
        # group profiles
        else:
            r = await session.get(search.group('clean_url'), timeout=timeout)
            text = await r.text()
            data_match = re.search(r"OpenGroupChat\(\s*'(?P<steam_id>\d+)'", text)

            if data_match:
                return int(data_match.group('steam_id'))
    finally:
        await session.close()


def parse_trade_url_token(url: str) -> Optional[str]:
    """Parses a trade URL for an user's token.

    Parameters
    -----------
    url: :class:`str`
        The URL to search for a token.

    Returns
    -------
    Optional[:class:`str`]
        The found token or ``None`` if the URL doesn't match the regex.
    """
    search = re.search(r"(?:http[s]?://|)(?:www.|)steamcommunity.com/tradeoffer/new/\?partner=\d{7,}"
                       r"(?:&|&amp;)token=(?P<token>[\w-]{7,})", url)
    if search:
        return search.group('token')
    return None


def ainput(prompt: str = '', loop: asyncio.AbstractEventLoop = None) -> Awaitable:
    loop = loop or asyncio.get_running_loop()
    return loop.run_in_executor(None, input, prompt)


# everything below here is directly from discord.py's utils
# https://github.com/rapptz/discord.py/blob/master/discord/utils.py


def find(predicate: Callable[..., bool], iterable: Iterable) -> Optional[Any]:
    """A helper to return the first element found in the sequence.

    Parameters
    -----------
    predicate: Callable[..., bool]
        A function that returns a boolean.
    iterable: Iterable
        The iterable to search through.

    Returns
    -------
    Optional[Any]
        The first element from the ``iterable``
        for which the ``predicate`` returns ``True``
        or ``None`` if no matching element was found.
    """

    for element in iterable:
        if predicate(element):
            return element
    return None


def get(iterable: Iterable, **attrs) -> Optional[Any]:
    r"""A helper that returns the first element in the iterable that meets
    all the traits passed in ``attrs``. This is an alternative for
    :func:`utils.find`.

    Parameters
    -----------
    iterable: Iterable
        An iterable to search through.
    \*\*attrs
        Keyword arguments that denote attributes to match.

    Returns
    -------
    Optional[Any]
        The first element from the ``iterable``
        which matches all the traits passed in ``attrs``
        or ``None`` if no matching element was found.
    """

    # global -> local
    _all = all
    attrget = attrgetter

    # Special case the single element call
    if len(attrs) == 1:
        k, v = attrs.popitem()
        pred = attrget(k.replace('__', '.'))
        for elem in iterable:
            if pred(elem) == v:
                return elem
        return None

    converted = [
        (attrget(attr.replace('__', '.')), value)
        for attr, value in attrs.items()
    ]

    for elem in iterable:
        if _all(pred(elem) == value for pred, value in converted):
            return elem
    return None


async def maybe_coroutine(func: Union[Callable, Coroutine], *args, **kwargs) -> Any:
    func = func(*args, **kwargs)
    if asyncio.iscoroutinefunction(func):
        return await func
    return func

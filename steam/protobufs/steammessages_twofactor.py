# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_twofactor.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CTwoFactor_Status_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CTwoFactor_Status_Response(betterproto.Message):
    state: int = betterproto.uint32_field(1)
    inactivation_reason: int = betterproto.uint32_field(2)
    authenticator_type: int = betterproto.uint32_field(3)
    authenticator_allowed: bool = betterproto.bool_field(4)
    steamguard_scheme: int = betterproto.uint32_field(5)
    token_gid: str = betterproto.string_field(6)
    email_validated: bool = betterproto.bool_field(7)
    device_identifier: str = betterproto.string_field(8)
    time_created: int = betterproto.uint32_field(9)
    revocation_attempts_remaining: int = betterproto.uint32_field(10)
    classified_agent: str = betterproto.string_field(11)
    allow_external_authenticator: bool = betterproto.bool_field(12)
    time_transferred: int = betterproto.uint32_field(13)


@dataclass
class CTwoFactor_AddAuthenticator_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    authenticator_time: int = betterproto.uint64_field(2)
    serial_number: float = betterproto.fixed64_field(3)
    authenticator_type: int = betterproto.uint32_field(4)
    device_identifier: str = betterproto.string_field(5)
    sms_phone_id: str = betterproto.string_field(6)
    http_headers: List[str] = betterproto.string_field(7)


@dataclass
class CTwoFactor_AddAuthenticator_Response(betterproto.Message):
    shared_secret: bytes = betterproto.bytes_field(1)
    serial_number: float = betterproto.fixed64_field(2)
    revocation_code: str = betterproto.string_field(3)
    uri: str = betterproto.string_field(4)
    server_time: int = betterproto.uint64_field(5)
    account_name: str = betterproto.string_field(6)
    token_gid: str = betterproto.string_field(7)
    identity_secret: bytes = betterproto.bytes_field(8)
    secret_1: bytes = betterproto.bytes_field(9)
    status: int = betterproto.int32_field(10)


@dataclass
class CTwoFactor_SendEmail_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    email_type: int = betterproto.uint32_field(2)
    include_activation_code: bool = betterproto.bool_field(3)


@dataclass
class CTwoFactor_SendEmail_Response(betterproto.Message):
    pass


@dataclass
class CTwoFactor_FinalizeAddAuthenticator_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    authenticator_code: str = betterproto.string_field(2)
    authenticator_time: int = betterproto.uint64_field(3)
    activation_code: str = betterproto.string_field(4)
    http_headers: List[str] = betterproto.string_field(5)


@dataclass
class CTwoFactor_FinalizeAddAuthenticator_Response(betterproto.Message):
    success: bool = betterproto.bool_field(1)
    want_more: bool = betterproto.bool_field(2)
    server_time: int = betterproto.uint64_field(3)
    status: int = betterproto.int32_field(4)


@dataclass
class CTwoFactor_RemoveAuthenticator_Request(betterproto.Message):
    revocation_code: str = betterproto.string_field(2)
    revocation_reason: int = betterproto.uint32_field(5)
    steamguard_scheme: int = betterproto.uint32_field(6)
    remove_all_steamguard_cookies: bool = betterproto.bool_field(7)


@dataclass
class CTwoFactor_RemoveAuthenticator_Response(betterproto.Message):
    success: bool = betterproto.bool_field(1)
    server_time: int = betterproto.uint64_field(3)
    revocation_attempts_remaining: int = betterproto.uint32_field(5)


@dataclass
class CTwoFactor_CreateEmergencyCodes_Request(betterproto.Message):
    code: str = betterproto.string_field(1)


@dataclass
class CTwoFactor_CreateEmergencyCodes_Response(betterproto.Message):
    codes: List[str] = betterproto.string_field(1)


@dataclass
class CTwoFactor_DestroyEmergencyCodes_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)


@dataclass
class CTwoFactor_DestroyEmergencyCodes_Response(betterproto.Message):
    pass


@dataclass
class CTwoFactor_ValidateToken_Request(betterproto.Message):
    code: str = betterproto.string_field(1)


@dataclass
class CTwoFactor_ValidateToken_Response(betterproto.Message):
    valid: bool = betterproto.bool_field(1)

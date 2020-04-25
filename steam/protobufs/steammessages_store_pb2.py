# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_store.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='steammessages_store.proto',
    package='',
    syntax='proto2',
    serialized_options=_b('\220\001\001'),
    serialized_pb=_b(
        '\n\x19steammessages_store.proto\x1a steammessages_unified_base.proto\"J\n&CStore_GetLocalizedNameForTags_Request\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0e\n\x06tagids\x18\x02 \x03(\r\"\x9f\x01\n\'CStore_GetLocalizedNameForTags_Response\x12:\n\x04tags\x18\x01 \x03(\x0b\x32,.CStore_GetLocalizedNameForTags_Response.Tag\x1a\x38\n\x03Tag\x12\r\n\x05tagid\x18\x01 \x01(\r\x12\x14\n\x0c\x65nglish_name\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"$\n\"CStore_GetStorePreferences_Request\"\xb1\x03\n\x16\x43Store_UserPreferences\x12\x18\n\x10primary_language\x18\x01 \x01(\r\x12\x1b\n\x13secondary_languages\x18\x02 \x01(\r\x12\x18\n\x10platform_windows\x18\x03 \x01(\x08\x12\x14\n\x0cplatform_mac\x18\x04 \x01(\x08\x12\x16\n\x0eplatform_linux\x18\x05 \x01(\x08\x12#\n\x1bhide_adult_content_violence\x18\x06 \x01(\x08\x12\x1e\n\x16hide_adult_content_sex\x18\x07 \x01(\x08\x12\x19\n\x11timestamp_updated\x18\x08 \x01(\r\x12\x1c\n\x14hide_store_broadcast\x18\t \x01(\x08\x12`\n\x17review_score_preference\x18\n \x01(\x0e\x32\x1b.EUserReviewScorePreference:\"k_EUserReviewScorePreference_Unset\x12\x38\n0timestamp_content_descriptor_preferences_updated\x18\x0b \x01(\x05\"\x91\x01\n\x19\x43Store_UserTagPreferences\x12\x37\n\x0ftags_to_exclude\x18\x01 \x03(\x0b\x32\x1e.CStore_UserTagPreferences.Tag\x1a;\n\x03Tag\x12\r\n\x05tagid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0ftimestamp_added\x18\x03 \x01(\r\"\xd9\x01\n\'CStore_UserContentDescriptorPreferences\x12\x62\n\x1e\x63ontent_descriptors_to_exclude\x18\x01 \x03(\x0b\x32:.CStore_UserContentDescriptorPreferences.ContentDescriptor\x1aJ\n\x11\x43ontentDescriptor\x12\x1c\n\x14\x63ontent_descriptorid\x18\x01 \x01(\r\x12\x17\n\x0ftimestamp_added\x18\x02 \x01(\r\"\xda\x01\n#CStore_GetStorePreferences_Response\x12,\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x17.CStore_UserPreferences\x12\x33\n\x0ftag_preferences\x18\x02 \x01(\x0b\x32\x1a.CStore_UserTagPreferences\x12P\n\x1e\x63ontent_descriptor_preferences\x18\x03 \x01(\x0b\x32(.CStore_UserContentDescriptorPreferences\"\xe2\x01\n+CStore_StorePreferencesChanged_Notification\x12,\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x17.CStore_UserPreferences\x12\x33\n\x0ftag_preferences\x18\x02 \x01(\x0b\x32\x1a.CStore_UserTagPreferences\x12P\n\x1e\x63ontent_descriptor_preferences\x18\x03 \x01(\x0b\x32(.CStore_UserContentDescriptorPreferences*\xa0\x01\n\x1a\x45UserReviewScorePreference\x12&\n\"k_EUserReviewScorePreference_Unset\x10\x00\x12+\n\'k_EUserReviewScorePreference_IncludeAll\x10\x01\x12-\n)k_EUserReviewScorePreference_ExcludeBombs\x10\x02\x32\xf9\x02\n\x05Store\x12\x98\x01\n\x17GetLocalizedNameForTags\x12\'.CStore_GetLocalizedNameForTags_Request\x1a(.CStore_GetLocalizedNameForTags_Response\"*\x82\xb5\x18&Gets tag names in a different language\x12\xaf\x01\n\x13GetStorePreferences\x12#.CStore_GetStorePreferences_Request\x1a$.CStore_GetStorePreferences_Response\"M\x82\xb5\x18IReturns the desired ratings board and maximum rating to show on the store\x1a#\x82\xb5\x18\x1f\x41 service to access store data.2\xee\x01\n\x0bStoreClient\x12\xb1\x01\n\x1dNotifyStorePreferencesChanged\x12,.CStore_StorePreferencesChanged_Notification\x1a\x0b.NoResponse\"U\x82\xb5\x18QNotification from server to client that the user\'s store preferences have changed\x1a+\x82\xb5\x18#Steam store to client notifications\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')
    ,
    dependencies=[steammessages__unified__base__pb2.DESCRIPTOR, ])

_EUSERREVIEWSCOREPREFERENCE = _descriptor.EnumDescriptor(
    name='EUserReviewScorePreference',
    full_name='EUserReviewScorePreference',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='k_EUserReviewScorePreference_Unset', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='k_EUserReviewScorePreference_IncludeAll', index=1, number=1,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='k_EUserReviewScorePreference_ExcludeBombs', index=2, number=2,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1594,
    serialized_end=1754,
)
_sym_db.RegisterEnumDescriptor(_EUSERREVIEWSCOREPREFERENCE)

EUserReviewScorePreference = enum_type_wrapper.EnumTypeWrapper(_EUSERREVIEWSCOREPREFERENCE)
k_EUserReviewScorePreference_Unset = 0
k_EUserReviewScorePreference_IncludeAll = 1
k_EUserReviewScorePreference_ExcludeBombs = 2

_CSTORE_GETLOCALIZEDNAMEFORTAGS_REQUEST = _descriptor.Descriptor(
    name='CStore_GetLocalizedNameForTags_Request',
    full_name='CStore_GetLocalizedNameForTags_Request',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='language', full_name='CStore_GetLocalizedNameForTags_Request.language', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tagids', full_name='CStore_GetLocalizedNameForTags_Request.tagids', index=1,
            number=2, type=13, cpp_type=3, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=63,
    serialized_end=137,
)

_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE_TAG = _descriptor.Descriptor(
    name='Tag',
    full_name='CStore_GetLocalizedNameForTags_Response.Tag',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='tagid', full_name='CStore_GetLocalizedNameForTags_Response.Tag.tagid', index=0,
            number=1, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='english_name', full_name='CStore_GetLocalizedNameForTags_Response.Tag.english_name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='name', full_name='CStore_GetLocalizedNameForTags_Response.Tag.name', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=243,
    serialized_end=299,
)

_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE = _descriptor.Descriptor(
    name='CStore_GetLocalizedNameForTags_Response',
    full_name='CStore_GetLocalizedNameForTags_Response',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='tags', full_name='CStore_GetLocalizedNameForTags_Response.tags', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE_TAG, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=140,
    serialized_end=299,
)

_CSTORE_GETSTOREPREFERENCES_REQUEST = _descriptor.Descriptor(
    name='CStore_GetStorePreferences_Request',
    full_name='CStore_GetStorePreferences_Request',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=301,
    serialized_end=337,
)

_CSTORE_USERPREFERENCES = _descriptor.Descriptor(
    name='CStore_UserPreferences',
    full_name='CStore_UserPreferences',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='primary_language', full_name='CStore_UserPreferences.primary_language', index=0,
            number=1, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='secondary_languages', full_name='CStore_UserPreferences.secondary_languages', index=1,
            number=2, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='platform_windows', full_name='CStore_UserPreferences.platform_windows', index=2,
            number=3, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='platform_mac', full_name='CStore_UserPreferences.platform_mac', index=3,
            number=4, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='platform_linux', full_name='CStore_UserPreferences.platform_linux', index=4,
            number=5, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='hide_adult_content_violence', full_name='CStore_UserPreferences.hide_adult_content_violence', index=5,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='hide_adult_content_sex', full_name='CStore_UserPreferences.hide_adult_content_sex', index=6,
            number=7, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timestamp_updated', full_name='CStore_UserPreferences.timestamp_updated', index=7,
            number=8, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='hide_store_broadcast', full_name='CStore_UserPreferences.hide_store_broadcast', index=8,
            number=9, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='review_score_preference', full_name='CStore_UserPreferences.review_score_preference', index=9,
            number=10, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timestamp_content_descriptor_preferences_updated',
            full_name='CStore_UserPreferences.timestamp_content_descriptor_preferences_updated', index=10,
            number=11, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=340,
    serialized_end=773,
)

_CSTORE_USERTAGPREFERENCES_TAG = _descriptor.Descriptor(
    name='Tag',
    full_name='CStore_UserTagPreferences.Tag',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='tagid', full_name='CStore_UserTagPreferences.Tag.tagid', index=0,
            number=1, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='name', full_name='CStore_UserTagPreferences.Tag.name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timestamp_added', full_name='CStore_UserTagPreferences.Tag.timestamp_added', index=2,
            number=3, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=862,
    serialized_end=921,
)

_CSTORE_USERTAGPREFERENCES = _descriptor.Descriptor(
    name='CStore_UserTagPreferences',
    full_name='CStore_UserTagPreferences',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='tags_to_exclude', full_name='CStore_UserTagPreferences.tags_to_exclude', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_CSTORE_USERTAGPREFERENCES_TAG, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=776,
    serialized_end=921,
)

_CSTORE_USERCONTENTDESCRIPTORPREFERENCES_CONTENTDESCRIPTOR = _descriptor.Descriptor(
    name='ContentDescriptor',
    full_name='CStore_UserContentDescriptorPreferences.ContentDescriptor',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='content_descriptorid',
            full_name='CStore_UserContentDescriptorPreferences.ContentDescriptor.content_descriptorid', index=0,
            number=1, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timestamp_added',
            full_name='CStore_UserContentDescriptorPreferences.ContentDescriptor.timestamp_added', index=1,
            number=2, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1067,
    serialized_end=1141,
)

_CSTORE_USERCONTENTDESCRIPTORPREFERENCES = _descriptor.Descriptor(
    name='CStore_UserContentDescriptorPreferences',
    full_name='CStore_UserContentDescriptorPreferences',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='content_descriptors_to_exclude',
            full_name='CStore_UserContentDescriptorPreferences.content_descriptors_to_exclude', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_CSTORE_USERCONTENTDESCRIPTORPREFERENCES_CONTENTDESCRIPTOR, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=924,
    serialized_end=1141,
)

_CSTORE_GETSTOREPREFERENCES_RESPONSE = _descriptor.Descriptor(
    name='CStore_GetStorePreferences_Response',
    full_name='CStore_GetStorePreferences_Response',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='preferences', full_name='CStore_GetStorePreferences_Response.preferences', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tag_preferences', full_name='CStore_GetStorePreferences_Response.tag_preferences', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='content_descriptor_preferences',
            full_name='CStore_GetStorePreferences_Response.content_descriptor_preferences', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1144,
    serialized_end=1362,
)

_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION = _descriptor.Descriptor(
    name='CStore_StorePreferencesChanged_Notification',
    full_name='CStore_StorePreferencesChanged_Notification',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='preferences', full_name='CStore_StorePreferencesChanged_Notification.preferences', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tag_preferences', full_name='CStore_StorePreferencesChanged_Notification.tag_preferences', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='content_descriptor_preferences',
            full_name='CStore_StorePreferencesChanged_Notification.content_descriptor_preferences', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1365,
    serialized_end=1591,
)

_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE_TAG.containing_type = _CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE
_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE.fields_by_name[
    'tags'].message_type = _CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE_TAG
_CSTORE_USERPREFERENCES.fields_by_name['review_score_preference'].enum_type = _EUSERREVIEWSCOREPREFERENCE
_CSTORE_USERTAGPREFERENCES_TAG.containing_type = _CSTORE_USERTAGPREFERENCES
_CSTORE_USERTAGPREFERENCES.fields_by_name['tags_to_exclude'].message_type = _CSTORE_USERTAGPREFERENCES_TAG
_CSTORE_USERCONTENTDESCRIPTORPREFERENCES_CONTENTDESCRIPTOR.containing_type = _CSTORE_USERCONTENTDESCRIPTORPREFERENCES
_CSTORE_USERCONTENTDESCRIPTORPREFERENCES.fields_by_name[
    'content_descriptors_to_exclude'].message_type = _CSTORE_USERCONTENTDESCRIPTORPREFERENCES_CONTENTDESCRIPTOR
_CSTORE_GETSTOREPREFERENCES_RESPONSE.fields_by_name['preferences'].message_type = _CSTORE_USERPREFERENCES
_CSTORE_GETSTOREPREFERENCES_RESPONSE.fields_by_name['tag_preferences'].message_type = _CSTORE_USERTAGPREFERENCES
_CSTORE_GETSTOREPREFERENCES_RESPONSE.fields_by_name[
    'content_descriptor_preferences'].message_type = _CSTORE_USERCONTENTDESCRIPTORPREFERENCES
_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION.fields_by_name['preferences'].message_type = _CSTORE_USERPREFERENCES
_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION.fields_by_name['tag_preferences'].message_type = _CSTORE_USERTAGPREFERENCES
_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION.fields_by_name[
    'content_descriptor_preferences'].message_type = _CSTORE_USERCONTENTDESCRIPTORPREFERENCES
DESCRIPTOR.message_types_by_name['CStore_GetLocalizedNameForTags_Request'] = _CSTORE_GETLOCALIZEDNAMEFORTAGS_REQUEST
DESCRIPTOR.message_types_by_name['CStore_GetLocalizedNameForTags_Response'] = _CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE
DESCRIPTOR.message_types_by_name['CStore_GetStorePreferences_Request'] = _CSTORE_GETSTOREPREFERENCES_REQUEST
DESCRIPTOR.message_types_by_name['CStore_UserPreferences'] = _CSTORE_USERPREFERENCES
DESCRIPTOR.message_types_by_name['CStore_UserTagPreferences'] = _CSTORE_USERTAGPREFERENCES
DESCRIPTOR.message_types_by_name['CStore_UserContentDescriptorPreferences'] = _CSTORE_USERCONTENTDESCRIPTORPREFERENCES
DESCRIPTOR.message_types_by_name['CStore_GetStorePreferences_Response'] = _CSTORE_GETSTOREPREFERENCES_RESPONSE
DESCRIPTOR.message_types_by_name[
    'CStore_StorePreferencesChanged_Notification'] = _CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION
DESCRIPTOR.enum_types_by_name['EUserReviewScorePreference'] = _EUSERREVIEWSCOREPREFERENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CStore_GetLocalizedNameForTags_Request = _reflection.GeneratedProtocolMessageType(
    'CStore_GetLocalizedNameForTags_Request', (_message.Message,), dict(
        DESCRIPTOR=_CSTORE_GETLOCALIZEDNAMEFORTAGS_REQUEST,
        __module__='steammessages_store_pb2'
        # @@protoc_insertion_point(class_scope:CStore_GetLocalizedNameForTags_Request)
    ))
_sym_db.RegisterMessage(CStore_GetLocalizedNameForTags_Request)

CStore_GetLocalizedNameForTags_Response = _reflection.GeneratedProtocolMessageType(
    'CStore_GetLocalizedNameForTags_Response', (_message.Message,), dict(

        Tag=_reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), dict(
            DESCRIPTOR=_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE_TAG,
            __module__='steammessages_store_pb2'
            # @@protoc_insertion_point(class_scope:CStore_GetLocalizedNameForTags_Response.Tag)
        ))
        ,
        DESCRIPTOR=_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE,
        __module__='steammessages_store_pb2'
        # @@protoc_insertion_point(class_scope:CStore_GetLocalizedNameForTags_Response)
    ))
_sym_db.RegisterMessage(CStore_GetLocalizedNameForTags_Response)
_sym_db.RegisterMessage(CStore_GetLocalizedNameForTags_Response.Tag)

CStore_GetStorePreferences_Request = _reflection.GeneratedProtocolMessageType('CStore_GetStorePreferences_Request',
                                                                              (_message.Message,), dict(
        DESCRIPTOR=_CSTORE_GETSTOREPREFERENCES_REQUEST,
        __module__='steammessages_store_pb2'
        # @@protoc_insertion_point(class_scope:CStore_GetStorePreferences_Request)
    ))
_sym_db.RegisterMessage(CStore_GetStorePreferences_Request)

CStore_UserPreferences = _reflection.GeneratedProtocolMessageType('CStore_UserPreferences', (_message.Message,), dict(
    DESCRIPTOR=_CSTORE_USERPREFERENCES,
    __module__='steammessages_store_pb2'
    # @@protoc_insertion_point(class_scope:CStore_UserPreferences)
))
_sym_db.RegisterMessage(CStore_UserPreferences)

CStore_UserTagPreferences = _reflection.GeneratedProtocolMessageType('CStore_UserTagPreferences', (_message.Message,),
                                                                     dict(

                                                                         Tag=_reflection.GeneratedProtocolMessageType(
                                                                             'Tag', (_message.Message,), dict(
                                                                                 DESCRIPTOR=_CSTORE_USERTAGPREFERENCES_TAG,
                                                                                 __module__='steammessages_store_pb2'
                                                                                 # @@protoc_insertion_point(class_scope:CStore_UserTagPreferences.Tag)
                                                                             ))
                                                                         ,
                                                                         DESCRIPTOR=_CSTORE_USERTAGPREFERENCES,
                                                                         __module__='steammessages_store_pb2'
                                                                         # @@protoc_insertion_point(class_scope:CStore_UserTagPreferences)
                                                                     ))
_sym_db.RegisterMessage(CStore_UserTagPreferences)
_sym_db.RegisterMessage(CStore_UserTagPreferences.Tag)

CStore_UserContentDescriptorPreferences = _reflection.GeneratedProtocolMessageType(
    'CStore_UserContentDescriptorPreferences', (_message.Message,), dict(

        ContentDescriptor=_reflection.GeneratedProtocolMessageType('ContentDescriptor', (_message.Message,), dict(
            DESCRIPTOR=_CSTORE_USERCONTENTDESCRIPTORPREFERENCES_CONTENTDESCRIPTOR,
            __module__='steammessages_store_pb2'
            # @@protoc_insertion_point(class_scope:CStore_UserContentDescriptorPreferences.ContentDescriptor)
        ))
        ,
        DESCRIPTOR=_CSTORE_USERCONTENTDESCRIPTORPREFERENCES,
        __module__='steammessages_store_pb2'
        # @@protoc_insertion_point(class_scope:CStore_UserContentDescriptorPreferences)
    ))
_sym_db.RegisterMessage(CStore_UserContentDescriptorPreferences)
_sym_db.RegisterMessage(CStore_UserContentDescriptorPreferences.ContentDescriptor)

CStore_GetStorePreferences_Response = _reflection.GeneratedProtocolMessageType('CStore_GetStorePreferences_Response',
                                                                               (_message.Message,), dict(
        DESCRIPTOR=_CSTORE_GETSTOREPREFERENCES_RESPONSE,
        __module__='steammessages_store_pb2'
        # @@protoc_insertion_point(class_scope:CStore_GetStorePreferences_Response)
    ))
_sym_db.RegisterMessage(CStore_GetStorePreferences_Response)

CStore_StorePreferencesChanged_Notification = _reflection.GeneratedProtocolMessageType(
    'CStore_StorePreferencesChanged_Notification', (_message.Message,), dict(
        DESCRIPTOR=_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION,
        __module__='steammessages_store_pb2'
        # @@protoc_insertion_point(class_scope:CStore_StorePreferencesChanged_Notification)
    ))
_sym_db.RegisterMessage(CStore_StorePreferencesChanged_Notification)

DESCRIPTOR._options = None

_STORE = _descriptor.ServiceDescriptor(
    name='Store',
    full_name='Store',
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b('\202\265\030\037A service to access store data.'),
    serialized_start=1757,
    serialized_end=2134,
    methods=[
        _descriptor.MethodDescriptor(
            name='GetLocalizedNameForTags',
            full_name='Store.GetLocalizedNameForTags',
            index=0,
            containing_service=None,
            input_type=_CSTORE_GETLOCALIZEDNAMEFORTAGS_REQUEST,
            output_type=_CSTORE_GETLOCALIZEDNAMEFORTAGS_RESPONSE,
            serialized_options=_b('\202\265\030&Gets tag names in a different language'),
        ),
        _descriptor.MethodDescriptor(
            name='GetStorePreferences',
            full_name='Store.GetStorePreferences',
            index=1,
            containing_service=None,
            input_type=_CSTORE_GETSTOREPREFERENCES_REQUEST,
            output_type=_CSTORE_GETSTOREPREFERENCES_RESPONSE,
            serialized_options=_b(
                '\202\265\030IReturns the desired ratings board and maximum rating to show on the store'),
        ),
    ])
_sym_db.RegisterServiceDescriptor(_STORE)

DESCRIPTOR.services_by_name['Store'] = _STORE

_STORECLIENT = _descriptor.ServiceDescriptor(
    name='StoreClient',
    full_name='StoreClient',
    file=DESCRIPTOR,
    index=1,
    serialized_options=_b('\202\265\030#Steam store to client notifications\300\265\030\002'),
    serialized_start=2137,
    serialized_end=2375,
    methods=[
        _descriptor.MethodDescriptor(
            name='NotifyStorePreferencesChanged',
            full_name='StoreClient.NotifyStorePreferencesChanged',
            index=0,
            containing_service=None,
            input_type=_CSTORE_STOREPREFERENCESCHANGED_NOTIFICATION,
            output_type=steammessages__unified__base__pb2._NORESPONSE,
            serialized_options=_b(
                '\202\265\030QNotification from server to client that the user\'s store preferences have changed'),
        ),
    ])
_sym_db.RegisterServiceDescriptor(_STORECLIENT)

DESCRIPTOR.services_by_name['StoreClient'] = _STORECLIENT

Store = service_reflection.GeneratedServiceType('Store', (_service.Service,), dict(
    DESCRIPTOR=_STORE,
    __module__='steammessages_store_pb2'
))

Store_Stub = service_reflection.GeneratedServiceStubType('Store_Stub', (Store,), dict(
    DESCRIPTOR=_STORE,
    __module__='steammessages_store_pb2'
))

StoreClient = service_reflection.GeneratedServiceType('StoreClient', (_service.Service,), dict(
    DESCRIPTOR=_STORECLIENT,
    __module__='steammessages_store_pb2'
))

StoreClient_Stub = service_reflection.GeneratedServiceStubType('StoreClient_Stub', (StoreClient,), dict(
    DESCRIPTOR=_STORECLIENT,
    __module__='steammessages_store_pb2'
))

# @@protoc_insertion_point(module_scope)

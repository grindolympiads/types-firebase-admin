import json
from _typeshed import Incomplete

class Message:
    data: Incomplete
    notification: Incomplete
    android: Incomplete
    webpush: Incomplete
    apns: Incomplete
    fcm_options: Incomplete
    token: Incomplete
    topic: Incomplete
    condition: Incomplete
    def __init__(self, data: Incomplete | None = None, notification: Incomplete | None = None, android: Incomplete | None = None, webpush: Incomplete | None = None, apns: Incomplete | None = None, fcm_options: Incomplete | None = None, token: Incomplete | None = None, topic: Incomplete | None = None, condition: Incomplete | None = None) -> None: ...

class MulticastMessage:
    tokens: Incomplete
    data: Incomplete
    notification: Incomplete
    android: Incomplete
    webpush: Incomplete
    apns: Incomplete
    fcm_options: Incomplete
    def __init__(self, tokens, data: Incomplete | None = None, notification: Incomplete | None = None, android: Incomplete | None = None, webpush: Incomplete | None = None, apns: Incomplete | None = None, fcm_options: Incomplete | None = None) -> None: ...

class _Validators:
    @classmethod
    def check_string(cls, label, value, non_empty: bool = False): ...
    @classmethod
    def check_number(cls, label, value): ...
    @classmethod
    def check_string_dict(cls, label, value): ...
    @classmethod
    def check_string_list(cls, label, value): ...
    @classmethod
    def check_number_list(cls, label, value): ...
    @classmethod
    def check_analytics_label(cls, label, value): ...
    @classmethod
    def check_boolean(cls, label, value): ...
    @classmethod
    def check_datetime(cls, label, value): ...

class MessageEncoder(json.JSONEncoder):
    @classmethod
    def remove_null_values(cls, dict_value): ...
    @classmethod
    def encode_android(cls, android): ...
    @classmethod
    def encode_android_fcm_options(cls, fcm_options): ...
    @classmethod
    def encode_ttl(cls, ttl): ...
    @classmethod
    def encode_milliseconds(cls, label, msec): ...
    @classmethod
    def encode_android_notification(cls, notification): ...
    @classmethod
    def encode_light_settings(cls, light_settings): ...
    @classmethod
    def encode_webpush(cls, webpush): ...
    @classmethod
    def encode_webpush_notification(cls, notification): ...
    @classmethod
    def encode_webpush_notification_actions(cls, actions): ...
    @classmethod
    def encode_webpush_fcm_options(cls, options): ...
    @classmethod
    def encode_apns(cls, apns): ...
    @classmethod
    def encode_apns_payload(cls, payload): ...
    @classmethod
    def encode_apns_fcm_options(cls, fcm_options): ...
    @classmethod
    def encode_aps(cls, aps): ...
    @classmethod
    def encode_aps_sound(cls, sound): ...
    @classmethod
    def encode_aps_alert(cls, alert): ...
    @classmethod
    def encode_notification(cls, notification): ...
    @classmethod
    def sanitize_topic_name(cls, topic): ...
    def default(self, o): ...
    @classmethod
    def encode_fcm_options(cls, fcm_options): ...

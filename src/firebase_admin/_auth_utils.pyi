from _typeshed import Incomplete
from firebase_admin import exceptions as exceptions

EMULATOR_HOST_ENV_VAR: str
MAX_CLAIMS_PAYLOAD_SIZE: int
RESERVED_CLAIMS: Incomplete
VALID_EMAIL_ACTION_TYPES: Incomplete

class PageIterator:
    def __init__(self, current_page) -> None: ...
    def __next__(self): ...
    def __iter__(self): ...
    @property
    def items(self) -> None: ...

def get_emulator_host(): ...
def is_emulated(): ...
def validate_uid(uid, required: bool = False): ...
def validate_email(email, required: bool = False): ...
def validate_phone(phone, required: bool = False): ...
def validate_password(password, required: bool = False): ...
def validate_bytes(value, label, required: bool = False): ...
def validate_display_name(display_name, required: bool = False): ...
def validate_provider_id(provider_id, required: bool = True): ...
def validate_provider_uid(provider_uid, required: bool = True): ...
def validate_photo_url(photo_url, required: bool = False): ...
def validate_timestamp(timestamp, label, required: bool = False): ...
def validate_int(value, label, low: Incomplete | None = None, high: Incomplete | None = None): ...
def validate_string(value, label): ...
def validate_boolean(value, label): ...
def validate_custom_claims(custom_claims, required: bool = False): ...
def validate_action_type(action_type): ...
def validate_provider_ids(provider_ids, required: bool = False): ...
def build_update_mask(params): ...

class UidAlreadyExistsError(exceptions.AlreadyExistsError):
    default_message: str
    def __init__(self, message, cause, http_response) -> None: ...

class EmailAlreadyExistsError(exceptions.AlreadyExistsError):
    default_message: str
    def __init__(self, message, cause, http_response) -> None: ...

class InsufficientPermissionError(exceptions.PermissionDeniedError):
    default_message: str
    def __init__(self, message, cause, http_response) -> None: ...

class InvalidDynamicLinkDomainError(exceptions.InvalidArgumentError):
    default_message: str
    def __init__(self, message, cause, http_response) -> None: ...

class InvalidIdTokenError(exceptions.InvalidArgumentError):
    default_message: str
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class PhoneNumberAlreadyExistsError(exceptions.AlreadyExistsError):
    default_message: str
    def __init__(self, message, cause, http_response) -> None: ...

class UnexpectedResponseError(exceptions.UnknownError):
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class UserNotFoundError(exceptions.NotFoundError):
    default_message: str
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class EmailNotFoundError(exceptions.NotFoundError):
    default_message: str
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class TenantNotFoundError(exceptions.NotFoundError):
    default_message: str
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class TenantIdMismatchError(exceptions.InvalidArgumentError):
    def __init__(self, message) -> None: ...

class ConfigurationNotFoundError(exceptions.NotFoundError):
    default_message: str
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class UserDisabledError(exceptions.InvalidArgumentError):
    default_message: str
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class TooManyAttemptsTryLaterError(exceptions.ResourceExhaustedError):
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

class ResetPasswordExceedLimitError(exceptions.ResourceExhaustedError):
    def __init__(self, message, cause: Incomplete | None = None, http_response: Incomplete | None = None) -> None: ...

def handle_auth_backend_error(error): ...

from _typeshed import Incomplete

__all__ = ['ActionCodeSettings', 'CertificateFetchError', 'Client', 'ConfigurationNotFoundError', 'DELETE_ATTRIBUTE', 'EmailAlreadyExistsError', 'EmailNotFoundError', 'ErrorInfo', 'ExpiredIdTokenError', 'ExpiredSessionCookieError', 'ExportedUserRecord', 'DeleteUsersResult', 'GetUsersResult', 'ImportUserRecord', 'InsufficientPermissionError', 'InvalidDynamicLinkDomainError', 'InvalidIdTokenError', 'InvalidSessionCookieError', 'ListProviderConfigsPage', 'ListUsersPage', 'OIDCProviderConfig', 'PhoneNumberAlreadyExistsError', 'ProviderConfig', 'ResetPasswordExceedLimitError', 'RevokedIdTokenError', 'RevokedSessionCookieError', 'SAMLProviderConfig', 'TokenSignError', 'TooManyAttemptsTryLaterError', 'UidAlreadyExistsError', 'UnexpectedResponseError', 'UserDisabledError', 'UserImportHash', 'UserImportResult', 'UserInfo', 'UserMetadata', 'UserNotFoundError', 'UserProvider', 'UserRecord', 'UserIdentifier', 'UidIdentifier', 'EmailIdentifier', 'PhoneIdentifier', 'ProviderIdentifier', 'create_custom_token', 'create_oidc_provider_config', 'create_saml_provider_config', 'create_session_cookie', 'create_user', 'delete_oidc_provider_config', 'delete_saml_provider_config', 'delete_user', 'delete_users', 'generate_email_verification_link', 'generate_password_reset_link', 'generate_sign_in_with_email_link', 'get_oidc_provider_config', 'get_saml_provider_config', 'get_user', 'get_user_by_email', 'get_user_by_phone_number', 'get_users', 'import_users', 'list_saml_provider_configs', 'list_users', 'revoke_refresh_tokens', 'set_custom_user_claims', 'update_oidc_provider_config', 'update_saml_provider_config', 'update_user', 'verify_id_token', 'verify_session_cookie']

ActionCodeSettings: Incomplete
CertificateFetchError: Incomplete
Client: Incomplete
ConfigurationNotFoundError: Incomplete
DELETE_ATTRIBUTE: Incomplete
DeleteUsersResult: Incomplete
EmailAlreadyExistsError: Incomplete
EmailNotFoundError: Incomplete
ErrorInfo: Incomplete
ExpiredIdTokenError: Incomplete
ExpiredSessionCookieError: Incomplete
ExportedUserRecord: Incomplete
GetUsersResult: Incomplete
ImportUserRecord: Incomplete
InsufficientPermissionError: Incomplete
InvalidDynamicLinkDomainError: Incomplete
InvalidIdTokenError: Incomplete
InvalidSessionCookieError: Incomplete
ListProviderConfigsPage: Incomplete
ListUsersPage: Incomplete
OIDCProviderConfig: Incomplete
PhoneNumberAlreadyExistsError: Incomplete
ProviderConfig: Incomplete
ResetPasswordExceedLimitError: Incomplete
RevokedIdTokenError: Incomplete
RevokedSessionCookieError: Incomplete
SAMLProviderConfig: Incomplete
TokenSignError: Incomplete
TooManyAttemptsTryLaterError: Incomplete
UidAlreadyExistsError: Incomplete
UnexpectedResponseError: Incomplete
UserDisabledError: Incomplete
UserImportHash: Incomplete
UserImportResult: Incomplete
UserInfo: Incomplete
UserMetadata: Incomplete
UserNotFoundError: Incomplete
UserProvider: Incomplete
UserRecord: Incomplete
UserIdentifier: Incomplete
UidIdentifier: Incomplete
EmailIdentifier: Incomplete
PhoneIdentifier: Incomplete
ProviderIdentifier: Incomplete

def create_custom_token(uid, developer_claims: Incomplete | None = None, app: Incomplete | None = None): ...
def verify_id_token(id_token, app: Incomplete | None = None, check_revoked: bool = False, clock_skew_seconds: int = 0): ...
def create_session_cookie(id_token, expires_in, app: Incomplete | None = None): ...
def verify_session_cookie(session_cookie, check_revoked: bool = False, app: Incomplete | None = None, clock_skew_seconds: int = 0): ...
def revoke_refresh_tokens(uid, app: Incomplete | None = None) -> None: ...
def get_user(uid, app: Incomplete | None = None): ...
def get_user_by_email(email, app: Incomplete | None = None): ...
def get_user_by_phone_number(phone_number, app: Incomplete | None = None): ...
def get_users(identifiers, app: Incomplete | None = None): ...
def list_users(page_token: Incomplete | None = None, max_results=..., app: Incomplete | None = None): ...
def create_user(**kwargs): ...
def update_user(uid, **kwargs): ...
def set_custom_user_claims(uid, custom_claims, app: Incomplete | None = None) -> None: ...
def delete_user(uid, app: Incomplete | None = None) -> None: ...
def delete_users(uids, app: Incomplete | None = None): ...
def import_users(users, hash_alg: Incomplete | None = None, app: Incomplete | None = None): ...
def generate_password_reset_link(email, action_code_settings: Incomplete | None = None, app: Incomplete | None = None): ...
def generate_email_verification_link(email, action_code_settings: Incomplete | None = None, app: Incomplete | None = None): ...
def generate_sign_in_with_email_link(email, action_code_settings, app: Incomplete | None = None): ...
def get_oidc_provider_config(provider_id, app: Incomplete | None = None): ...
def create_oidc_provider_config(provider_id, client_id, issuer, display_name: Incomplete | None = None, enabled: Incomplete | None = None, client_secret: Incomplete | None = None, id_token_response_type: Incomplete | None = None, code_response_type: Incomplete | None = None, app: Incomplete | None = None): ...
def update_oidc_provider_config(provider_id, client_id: Incomplete | None = None, issuer: Incomplete | None = None, display_name: Incomplete | None = None, enabled: Incomplete | None = None, client_secret: Incomplete | None = None, id_token_response_type: Incomplete | None = None, code_response_type: Incomplete | None = None, app: Incomplete | None = None): ...
def delete_oidc_provider_config(provider_id, app: Incomplete | None = None) -> None: ...
def get_saml_provider_config(provider_id, app: Incomplete | None = None): ...
def create_saml_provider_config(provider_id, idp_entity_id, sso_url, x509_certificates, rp_entity_id, callback_url, display_name: Incomplete | None = None, enabled: Incomplete | None = None, app: Incomplete | None = None): ...
def update_saml_provider_config(provider_id, idp_entity_id: Incomplete | None = None, sso_url: Incomplete | None = None, x509_certificates: Incomplete | None = None, rp_entity_id: Incomplete | None = None, callback_url: Incomplete | None = None, display_name: Incomplete | None = None, enabled: Incomplete | None = None, app: Incomplete | None = None): ...
def delete_saml_provider_config(provider_id, app: Incomplete | None = None) -> None: ...
def list_saml_provider_configs(page_token: Incomplete | None = None, max_results=..., app: Incomplete | None = None): ...

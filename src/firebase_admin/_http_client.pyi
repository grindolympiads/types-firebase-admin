from _typeshed import Incomplete

DEFAULT_RETRY_CONFIG: Incomplete
DEFAULT_TIMEOUT_SECONDS: int
METRICS_HEADERS: Incomplete

class HttpClient:
    def __init__(self, credential: Incomplete | None = None, session: Incomplete | None = None, base_url: str = '', headers: Incomplete | None = None, retries=..., timeout=...) -> None: ...
    @property
    def session(self): ...
    @property
    def base_url(self): ...
    @property
    def timeout(self): ...
    def parse_body(self, resp) -> None: ...
    def request(self, method, url, **kwargs): ...
    def headers(self, method, url, **kwargs): ...
    def body_and_response(self, method, url, **kwargs): ...
    def body(self, method, url, **kwargs): ...
    def headers_and_body(self, method, url, **kwargs): ...
    def close(self) -> None: ...

class JsonHttpClient(HttpClient):
    def __init__(self, **kwargs) -> None: ...
    def parse_body(self, resp): ...

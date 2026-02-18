from dataclasses import dataclass
from typing import Any, Dict, IO, Literal, Optional, Tuple, Union, overload

import requests



@dataclass
class HttpServiceOptions:
    base_url: str
    default_timeout: float = 15.0


class HttpMethod:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


@dataclass
class HttpCallOptionsSimple:
    path: str
    token: Optional[str] = None
    method: str = HttpMethod.GET
    timeout: Optional[float] = None
    query: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None


class HttpService:
    def __init__(self, options: HttpServiceOptions):
        self._base_url = options.base_url.rstrip("/") + "/"
        self._default_timeout = options.default_timeout
        self._session = requests.Session()

    def _build_headers(self, call: HttpCallOptionsSimple) -> Dict[str, str]:
        headers = get_headers(
            include_token=bool(call.token),
            bearer_token=call.token
        )

        # Add a normal user-agent (helps with some WAF/proxy setups)
        headers.setdefault("User-Agent", "Mozilla/5.0")

        # Content-Type is unnecessary (and sometimes harmful) for GET/DELETE with no body
        if call.method in (HttpMethod.GET, HttpMethod.DELETE) and "Content-Type" in headers:
            headers.pop("Content-Type", None)

        if call.headers:
            headers.update(call.headers)

        return headers


    def _url(self, path: str) -> str:
        return self._base_url + path.lstrip("/")

    @overload
    def call_without_body(
        self,
        call: HttpCallOptionsSimple,
        *,
        return_type: Literal["response"],
    ) -> requests.Response:
        ...

    @overload
    def call_without_body(
        self,
        call: HttpCallOptionsSimple,
        *,
        return_type: Literal["text"],
    ) -> str:
        ...

    @overload
    def call_without_body(
        self,
        call: HttpCallOptionsSimple,
        *,
        return_type: str = "json",
    ) -> Dict[str, Any]:
        ...

    def call_without_body(
        self,
        call: HttpCallOptionsSimple,
        *,
        return_type: str = "json",
    ) -> Union[requests.Response, str, Dict[str, Any]]:
        url = self._url(call.path)
        headers = self._build_headers(call)
        timeout = call.timeout if call.timeout is not None else self._default_timeout

        method = getattr(call, "method", None) or HttpMethod.GET

        response = self._session.request(
            method=method,
            url=url,
            headers=headers,
            params=call.query,
            timeout=timeout,
        )

      #  response.raise_for_status()

        if return_type == "response":
            return response
        if return_type == "text":
            return response.text
        return response.json()
    
    @overload
    def call_with_body(
        self,
        call: HttpCallOptionsSimple,
        body: Dict[str, Any],
        *,
        return_type: Literal["response"] = "response",
    ) -> requests.Response:
        ...

    @overload
    def call_with_body(
        self,
        call: HttpCallOptionsSimple,
        body: Dict[str, Any],
        *,
        return_type: Literal["text"],
    ) -> str:
        ...

    @overload
    def call_with_body(
        self,
        call: HttpCallOptionsSimple,
        body: Dict[str, Any],
        *,
        return_type: str,
    ) -> Dict[str, Any]:
        ...

    def call_with_body(
        self,
        call: HttpCallOptionsSimple,
        body: Dict[str, Any],
        *,
        return_type: str = "response",
    ) -> Union[requests.Response, str, Dict[str, Any]]:
        url = self._url(call.path)
        headers = self._build_headers(call)
        timeout = call.timeout if call.timeout is not None else self._default_timeout

        response = self._session.request(
            method=call.method,
            url=url,
            headers=headers,
            json=body,
            params=call.query,
            timeout=timeout,
        )

      # response.raise_for_status()

        if return_type == "response":
            return response
        if return_type == "text":
            return response.text
        return response.json()

    @overload
    def post(
        self,
        end_point: str,
        body: Dict[str, Any],
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        return_type: Literal["response"] = "response",
    ) -> requests.Response:
        ...

    @overload
    def post(
        self,
        end_point: str,
        body: Dict[str, Any],
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        return_type: Literal["text"],
    ) -> str:
        ...

    @overload
    def post(
        self,
        end_point: str,
        body: Dict[str, Any],
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        return_type: str,
    ) -> Dict[str, Any]:
        ...

    def post(
        self,
        end_point: str,
        body: Dict[str, Any],
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        return_type: str = "response",
    ) -> Union[requests.Response, str, Dict[str, Any]]:
        """POST to path with JSON body. Returns response object by default (use .json() for body)."""
        call = HttpCallOptionsSimple(
            path=end_point,
            method=HttpMethod.POST,
            token=token,
            timeout=timeout,
        )
        return self.call_with_body(call, body, return_type=return_type)

    @overload
    def get(
        self,
        end_point: str,
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        return_type: Literal["response"] = "response",
    ) -> requests.Response:
        ...

    @overload
    def get(
        self,
        end_point: str,
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        return_type: Literal["text"],
    ) -> str:
        ...

    @overload
    def get(
        self,
        end_point: str,
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        return_type: str,
    ) -> Dict[str, Any]:
        ...

    def get(
        self,
        end_point: str,
        *,
        token: Optional[str] = None,
        timeout: Optional[float] = None,
        query: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        return_type: str = "response",
    ) -> Union[requests.Response, str, Dict[str, Any]]:
        call = HttpCallOptionsSimple(
            path=end_point,
            method=HttpMethod.GET,
            token=token,
            timeout=timeout,
            query=query,
            headers=headers,
        )
        return self.call_without_body(call, return_type=return_type)
    
    @overload
    def call_form_data(
        self,
        call: HttpCallOptionsSimple,
        *,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Union[str, Tuple[str, Union[bytes, "IO[bytes]"], Optional[str]]]]] = None,
        return_type: Literal["response"] = "response",
    ) -> requests.Response:
        ...

    @overload
    def call_form_data(
        self,
        call: HttpCallOptionsSimple,
        *,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Union[str, Tuple[str, Union[bytes, "IO[bytes]"], Optional[str]]]]] = None,
        return_type: Literal["text"],
    ) -> str:
        ...

    @overload
    def call_form_data(
        self,
        call: HttpCallOptionsSimple,
        *,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Union[str, Tuple[str, Union[bytes, "IO[bytes]"], Optional[str]]]]] = None,
        return_type: str,
    ) -> Dict[str, Any]:
        ...

    def call_form_data(
        self,
        call: HttpCallOptionsSimple,
        *,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Union[str, Tuple[str, Union[bytes, "IO[bytes]"], Optional[str]]]]] = None,
        return_type: str = "response",
    ) -> Union[requests.Response, str, Dict[str, Any]]:


        url = self._url(call.path)
        headers = self._build_headers(call)
        timeout = call.timeout if call.timeout is not None else self._default_timeout

        # IMPORTANT: don't force content-type for multipart; requests sets it with boundary
        headers.pop("Content-Type", None)

        method = getattr(call, "method", None) or HttpMethod.POST

        # Normalize files to requests format
        prepared_files = None
        opened_files = []

        if files:
            prepared_files = {}
            for field, f in files.items():
                if isinstance(f, str):
                    # treat as filepath
                    fp = open(f, "rb")
                    opened_files.append(fp)
                    filename = f.split("\\")[-1]
                    prepared_files[field] = (filename, fp)
                elif isinstance(f, tuple):
                    # ("name.ext", bytes_or_fileobj, "mime/type"?) - mime optional
                    if len(f) == 2:
                        prepared_files[field] = (f[0], f[1])
                    elif len(f) == 3:
                        prepared_files[field] = (f[0], f[1], f[2])
                    else:
                        raise ValueError(
                            f"Invalid tuple for files['{field}']. Expected (filename, content) or (filename, content, content_type)."
                        )
                else:
                    raise ValueError(
                        f"Invalid value for files['{field}']. Use a filepath string or a tuple."
                    )

        try:
            response = self._session.request(
                method=method,
                url=url,
                headers=headers,
                data=data,              # form fields
                files=prepared_files,   # multipart files
                params=call.query,
                timeout=timeout,
            )
            response.raise_for_status()

            if return_type == "response":
                return response
            if return_type == "text":
                return response.text
            return response.json()

        finally:
            # Close any files we opened via filepath strings
            for fp in opened_files:
                try:
                    fp.close()
                except Exception:
                    pass



def get_headers(include_token=False, bearer_token=None):
    headers = {
        'Content-Type': 'application/json'
    }
    if include_token and bearer_token:
        headers['Authorization'] = f'Bearer {bearer_token}'
    return headers

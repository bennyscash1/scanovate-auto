from dataclasses import dataclass, asdict, fields
from typing import Any, Dict, Type, TypeVar

from ApiTest.HttpServices.base_api import BaseDTO

@dataclass
class AuthTokenInputDto(BaseDTO):
    client_id: str
    client_secret: str


@dataclass
class AuthTokenOutputDto(BaseDTO):
    access_token: str




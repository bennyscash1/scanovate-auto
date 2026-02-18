from dataclasses import dataclass
from ApiTest.HttpServices.base_api import BaseDTO


@dataclass
class GetFlowLinkOutputDto(BaseDTO):
    success: bool
    data: str
import requests
import sys
import os

from ApiTest.ApiFlows.AuthToken.AuthTokenDto import AuthTokenOutputDto
from ApiTest.ApiFlows.GetFlowLink.GetFlowLinkDto import GetFlowLinkOutputDto
from ApiTest.CommonApiService.api_services import ApiServices
from Infra.BaseData.GetData import VarData, loaded_data


def test_get_service():
    api_services = ApiServices()
    url_data= api_services.get_url_by_link(6668)





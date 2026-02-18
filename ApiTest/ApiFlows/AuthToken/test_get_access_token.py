from ApiTest.CommonApiService.api_services import ApiServices
from Infra.BaseData.CommonData import TestLevel
from Infra.BaseData.GetData import loaded_data, VarData
from ApiTest.HttpServices.http_requests import HttpService, HttpServiceOptions
@TestLevel.level0
def test_get_access_token():
    api_services = ApiServices()
    access_token = api_services.get_admin_token()
    assert access_token is not None
    assert isinstance(access_token, str)    
    


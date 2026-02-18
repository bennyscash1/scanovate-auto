
from ApiTest.ApiFlows.AuthToken.AuthTokenDto import AuthTokenInputDto, AuthTokenOutputDto
from ApiTest.ApiFlows.GetFlowLink.GetFlowLinkDto import GetFlowLinkOutputDto
from ApiTest.HttpServices.http_requests import HttpCallOptionsSimple, HttpService, HttpServiceOptions
from Infra.BaseData.GetData import VarData, loaded_data
import requests

class ApiServices:
    def get_admin_token(self, clientId: str = "",                       
                         clientSecret: str = "") -> str:
        
        clientId = clientId or loaded_data[VarData.ClientId]
        clientSecret = clientSecret or loaded_data[VarData.ClientSecret]
        
        self.svc = HttpService(HttpServiceOptions(base_url=loaded_data[VarData.BaseApiUrl]))
        payload = AuthTokenInputDto(client_id=clientId, client_secret=clientSecret)

        response = self.svc.post("auth/token", payload.to_dict(), return_type="response")
        assert response.status_code in (200, 201)
        response_dto = AuthTokenOutputDto.from_dict(response.json())
        access_token = response_dto.access_token
        return access_token
    
    def get_url_by_link(self, link_number: int) -> str:
        access_token = self.get_admin_token()
        get = HttpService(HttpServiceOptions(base_url=loaded_data[VarData.BaseApiUrl]))

        data = get.call_without_body(HttpCallOptionsSimple(
            path=f"flow/{link_number}/link", token=access_token))
        
        response_dto = GetFlowLinkOutputDto.from_dict(data)
        assert response_dto.success == True
        return response_dto.data



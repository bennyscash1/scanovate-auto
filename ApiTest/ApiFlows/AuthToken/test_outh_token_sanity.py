import pytest
from http import HTTPStatus
from ApiTest.ApiFlows.AuthToken.AuthTokenDto import AuthTokenInputDto
from Infra.BaseData.CommonData import TestLevel
from Infra.BaseData.GetData import loaded_data, VarData
from ApiTest.HttpServices.http_requests import HttpService, HttpServiceOptions


@pytest.mark.parametrize(
    "client_id, client_secret, expected_status",
    [
        pytest.param(loaded_data[VarData.ClientId], loaded_data[VarData.ClientSecret], HTTPStatus.OK, id="valid_credentials"),
        pytest.param("wrongClientId", loaded_data[VarData.ClientSecret], HTTPStatus.UNAUTHORIZED, id="invalid_client_id"),
        pytest.param(loaded_data[VarData.ClientId], "wrongSecret", HTTPStatus.UNAUTHORIZED, id="invalid_client_secret"),
        pytest.param("", loaded_data[VarData.ClientSecret], HTTPStatus.UNAUTHORIZED, id="empty_client_id"),
        pytest.param(loaded_data[VarData.ClientId], "", HTTPStatus.UNAUTHORIZED, id="empty_client_secret"),
        pytest.param(None, loaded_data[VarData.ClientSecret], HTTPStatus.BAD_REQUEST, id="none_client_id"),
        pytest.param(loaded_data[VarData.ClientId], None, HTTPStatus.BAD_REQUEST, id="none_client_secret"),
        pytest.param("wrongClientId", "wrongSecret", HTTPStatus.UNAUTHORIZED, id="both_invalid"),
    ],
)
@TestLevel.level0
def test_get_access_negative(client_id, client_secret, expected_status):
    svc = HttpService(
        HttpServiceOptions(base_url=loaded_data[VarData.BaseApiUrl])
    )
    payload = AuthTokenInputDto(
        client_id=client_id,
        client_secret=client_secret
    )

    response = svc.post("auth/token", payload.to_dict(),
        return_type="response"
    )
    assert response.status_code == expected_status

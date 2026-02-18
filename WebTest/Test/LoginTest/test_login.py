import os
import sys

import pytest

from Infra.BaseData import GetData
from WebTest.Flows.login_flow import LoginFlow
from WebTest.WebInfra.web_driver_factory import WebDriverFactory


@pytest.mark.webtest
class TestLoginWeb:
    def setup_method(self):
        self.driver = WebDriverFactory()
        self.page = self.driver.get_page()

        self.url = GetData.loaded_data[GetData.VarData.WebUrl]
        self.web_user_name = GetData.loaded_data[GetData.VarData.WebUserName]
        self.web_password = GetData.loaded_data[GetData.VarData.WebPassword]


    def test_login_web(self):
        login_flow = LoginFlow(self.page)
        login_flow.open_page(True, url=self.url)
        login_flow.login_web_flow(self.web_user_name, self.web_password)
        assert login_flow.is_eamil_display_on_dashboard(self.web_user_name) , "Login failed - User email not displayed on dashboard"

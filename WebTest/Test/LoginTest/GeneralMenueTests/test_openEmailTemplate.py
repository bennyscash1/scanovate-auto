from math import log
import os
import sys

import pytest

from Infra.BaseData import GetData
from WebTest.Flows.base_flows import SideBarMenue, SubMenuesList
from WebTest.Flows.login_flow import LoginFlow
from WebTest.WebInfra.web_driver_factory import WebDriverFactory


@pytest.mark.webtest
class TestLoginWeb:
    def setup_method(self):
        self.driver = WebDriverFactory()
        self.page = self.driver.get_page()

    def test_login_web(self):
        login_flow = LoginFlow(self.page)
        login_flow.login_with_default_user()

        login_flow.open_main_menue_side_bar(SideBarMenue.GENERAL)
        login_flow.open_sub_menue_side_bar(SubMenuesList.EMAIL_TEMPLATE)

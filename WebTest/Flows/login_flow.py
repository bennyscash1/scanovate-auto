from Infra.BaseData import GetData
from WebTest.Flows.base_flows import BaseFlows
from WebTest.PageObject.login_page import LoginPage


class LoginFlow(BaseFlows):

    def __init__(self, page):
        super().__init__(page)
        self.login_page = LoginPage(page)

    def web_login_flow(self, email: str, password: str):
        self.login_page.enter_email(email).enter_password(password).click_on_submit_button()
        return self

    def is_home_page_open(self) -> bool:
        return self.login_page.is_home_page_displayed()

    def login_with_default_user(self):
        self.url = GetData.loaded_data[GetData.VarData.WebUrl]
        self.web_user_name = GetData.loaded_data[GetData.VarData.WebUserName]
        self.web_password = GetData.loaded_data[GetData.VarData.WebPassword]
        self.open_page(True, url=self.url)
        self.web_login_flow(self.web_user_name, self.web_password)
        assert self.is_home_page_open(), "Login failed: Home page not displayed after login attempt."
        return self


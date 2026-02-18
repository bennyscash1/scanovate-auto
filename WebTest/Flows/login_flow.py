from WebTest.Flows.base_flows import BaseFlows
from WebTest.PageObject.login_page import LoginPage


class LoginFlow(BaseFlows):

    def __init__(self, page):
        super().__init__(page)
        self.login_page = LoginPage(page)

    def open_page(self, navigate_to_logon_screen=True, url=None):
        if navigate_to_logon_screen and url is not None:
            self.page.goto(url)  
        return self

    def web_login_flow(self, email: str, password: str):
        self.login_page.enter_email(email).enter_password(password).click_on_submit_button()
        return self

    def is_home_page_open(self) -> bool:
        return self.login_page.is_home_page_displayed()


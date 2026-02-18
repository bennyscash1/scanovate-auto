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

    def do_valid_login(self, email: str, password: str):
        self.login_page.enter_email(email).enter_password(password).click_on_submit_button()
        return self

    def login_web_flow(self, email: str, password: str):
        """Same as do_valid_login; for test compatibility."""
        return self.do_valid_login(email, password)

    def is_home_page_open(self) -> bool:
        return self.login_page.is_home_page_displayed()

    def is_eamil_display_on_dashboard(self, email: str) -> bool:
        """Check that login succeeded (home page or user email visible)."""
        return self.login_page.is_email_displayed_on_dashboard(email)

# Example of usage:
# driver = webdriver.Chrome()  # Or any other browser
# login_flow = LoginFlow(driver)
# login_flow.open_page(True, "http://example.com/login").do_valid_login("email@example.com", "password")
# print(login_flow.is_home_page_open())

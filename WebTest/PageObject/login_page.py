from playwright.sync_api import Page

from WebTest.PageObject.base_pages import BasePages


class LoginPage(BasePages):
    def __init__(self, page):
        super().__init__(page)
        self.m_user_name_input_field = "input#username"
        self.m_password_input_field = "input#password"
        self.m_submit_button = "button#submit"
        self.m_home_page_logo_by = "h1:has-text('Logged In Successfully')"
        self.m_dashboard_email_by = "p#username"  # element showing logged-in user

    def enter_email(self, email: str):
        self.fill_text(self.m_user_name_input_field, email)
        return self

    def enter_password(self, password: str):
        self.fill_text(self.m_password_input_field, password)
        return self

    def click_on_submit_button(self):
        self.click(self.m_submit_button)
        return self

    def is_home_page_displayed(self) -> bool:
        return self.is_element_found(self.m_home_page_logo_by)

    def is_email_displayed_on_dashboard(self, email: str) -> bool:
        return self.is_element_found(self.m_dashboard_email_by) or self.is_home_page_displayed()

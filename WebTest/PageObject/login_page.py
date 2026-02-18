from playwright.sync_api import Page

from WebTest.PageObject.base_pages import BasePages


class LoginPage(BasePages):
    def __init__(self, page):
        super().__init__(page)
        self.m_user_name_input_field = "//input[@id='name']"
        self.m_password_input_field = "//input[@id='password']"
        self.m_submit_button = "//button[@id='submit']"
        self.m_home_page_logo_by = "//img[@alt='btrust-logo']"
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
        logo_visible = self.is_element_display_with_retry(self.m_home_page_logo_by)
        if logo_visible:
            return True
        return self.is_element_display_with_retry(self.m_dashboard_email_by)


from MobileTest.MobileBasePage.mobile_base_pages import MobileBasePages


class MobileLoginPage(MobileBasePages):
    def __init__(self, driver):
        super().__init__(driver)
        #self.m_account_icon_by = ("xpath", "//android.widget.ImageButton[@content-desc=\"5\"]")

    def click_number_on_calculator(self, calculator_number):
        xpath = ( "xpath", f"//android.widget.ImageButton[@content-desc=\"{calculator_number}\"]" )
        self.mobile_click_element(xpath)
        return self


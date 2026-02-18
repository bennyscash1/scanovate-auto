from MobileTest.MobileFlow.nobile_base_flow import MobileBaseFlow
from  MobileTest.MobileBasePage.mobile_login_page import MobileLoginPage

class MobileLoginFlow(MobileBaseFlow):
    def __init__(self, driver):
        super().__init__(driver)
        self.mobile_login_page_object = MobileLoginPage(driver)

    def mobile_click_on_calculator(self, calculator_number):
        self.mobile_login_page_object.click_number_on_calculator(calculator_number)
        return self
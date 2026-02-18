import pytest
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))

sys.path.append(root_dir)

import Infra.BaseData as GetData
from MobileTest.InitialMobile.mobile_driver_factory import MobileDriverFactory
from MobileTest.MobileFlow.mobile_login_flow import MobileLoginFlow

class MobilaBasicTest(MobileDriverFactory):
    def __init__(self):
        super().__init__()
        self.contact_person = GetData.loaded_data[GetData.VarData.ContactName]
        self.contact_phone = GetData.loaded_data[GetData.VarData.ContactNumber]

    def test_mobile_basic_test(self):
        mobile_login_flow = MobileLoginFlow(self.appium_driver)
        mobile_login_flow.mobile_click_on_calculator(calculator_number = "2")

@pytest.mark.webtest
def test_contact():
    run_mobile= MobilaBasicTest()    
    run_mobile.test_mobile_basic_test()
    pass
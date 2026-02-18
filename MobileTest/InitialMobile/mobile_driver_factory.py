import subprocess
from appium.webdriver.webdriver import WebDriver
from appium.options.common import AppiumOptions

import Infra.BaseData as GetData


class MobileDriverFactory:
    def __init__(self):
        self.appium_driver = self.init_appium_driver()

    def create_appium_options(self):
        # Assuming GetData.loaded_data and GetData.VarData are defined and provide necessary configuration
        appPackage = GetData.loaded_data[GetData.VarData.AppPackage]
        appActivity = GetData.loaded_data[GetData.VarData.AppActivity]
        appUid = self.get_device_uuid()

        options = AppiumOptions()
        options.set_capability('platformName', 'Android')
        options.set_capability('deviceName', 'bennys9')
        options.set_capability('appPackage', appPackage)
        options.set_capability('appActivity', appActivity)
        options.set_capability('udid', appUid)
        return options

    def get_device_uuid(self):
        try:
            result = subprocess.run(["adb", "get-serialno"], capture_output=True, text=True, check=True)
            uuid = result.stdout.strip()
            return uuid
        except subprocess.CalledProcessError as e:
            print("Error executing adb:", e)
            return None
        
    def uninstall_uiautomator2(self):
        print("Uninstalling UiAutomator2 server packages...")
        subprocess.run(["adb", "uninstall", "io.appium.uiautomator2.server"], capture_output=True)
        subprocess.run(["adb", "uninstall", "io.appium.uiautomator2.server.test"], capture_output=True)


    def init_appium_driver(self, retry=True):
        try:
            options = self.create_appium_options()
            self.appium_driver = WebDriver(command_executor='http://127.0.0.1:4723/wd/hub', options=options)
            return self.appium_driver
        except Exception as e:
            print(f"Appium driver initialization failed: {e}")
            if retry:
                self.uninstall_uiautomator2()
                print("Retrying Appium driver initialization...")
                return self.init_appium_driver(retry=False)
            else:
                raise RuntimeError("Failed to initialize Appium driver after retrying.")

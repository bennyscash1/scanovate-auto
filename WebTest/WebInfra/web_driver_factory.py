from playwright.sync_api import sync_playwright

class WebDriverFactory:
    def __init__(self, browser_type: str = "chrome", headless: bool = False, device: str = None):
        self._playwright = sync_playwright().start()

        self.browser, self.page = self._launch_browser(
            browser_type=browser_type,
            headless=headless,
            device=device
        )

    def _launch_browser(self, browser_type: str, headless: bool, device: str):
        bt = (browser_type or "chrome").lower()

        if device:
            device_config = self._playwright.devices[device]
            browser = self._playwright.webkit.launch(headless=headless)
            context = browser.new_context(**device_config)
            page = context.new_page()
            return browser, page

        if bt in ("chrome", "chromium"):
            browser = self._playwright.chromium.launch(headless=headless)
        elif bt == "firefox":
            browser = self._playwright.firefox.launch(headless=headless)
        elif bt == "webkit":
            browser = self._playwright.webkit.launch(headless=headless)
        else:
            browser = self._playwright.chromium.launch(headless=headless)

        page = browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        return browser, page

    def get_page(self):
        return self.page

    def close_browser(self):
        try:
            if getattr(self, "browser", None):
                self.browser.close()
        finally:
            if getattr(self, "_playwright", None):
                self._playwright.stop()

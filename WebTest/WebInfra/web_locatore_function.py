from playwright.sync_api import Page


class WeblocatoreFunction:
    DEFAULT_TIMEOUT_MS = 20_000

    def __init__(self, page: Page):
        self.page = page

    def is_element_found(self, selector: str) -> bool:
        try:
            return self.page.locator(selector).is_visible(timeout=self.DEFAULT_TIMEOUT_MS)
        except Exception:
            return False

    def wait_for_element_visibility(self, selector: str) -> None:
        if not self.is_element_found(selector):
            raise AssertionError(
                f"Element {selector} not visible within {self.DEFAULT_TIMEOUT_MS / 1000}s"
            )

    def click(self, selector: str) -> None:
        self.page.locator(selector).click(timeout=self.DEFAULT_TIMEOUT_MS)

    def fill_text(self, selector: str, text: str) -> None:
        self.page.locator(selector).fill(text, timeout=self.DEFAULT_TIMEOUT_MS)

    def switch_to_frame(self, frame_selector: str):
        self.page.frame_locator(frame_selector)

    def is_displayed(self, selector: str) -> bool:
        return self.is_element_found(selector)

    def alert_ok(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def get_text_from_at(self, selector: str, attribute: str) -> str | None:
        self.wait_for_element_visibility(selector)
        return self.page.locator(selector).get_attribute(attribute)

    # def mark_element(self, selector):
    #     color = "#0000FF"
    #     element_handle = self.page.query_selector(selector)
    #     if element_handle:
    #         self.page.evaluate("element => element.style.border = '3px solid ' + arguments[1]", element_handle, color)

# Example of usage
# driver = webdriver.Chrome()  # Or any other browser you're using
# base_functions = BaseFunctions(driver)
# Remember to replace 'webdriver.Chrome()' with your actual WebDriver initialization.

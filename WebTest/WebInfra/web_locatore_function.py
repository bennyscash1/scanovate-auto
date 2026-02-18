import time

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class WeblocatoreFunction:
    DEFAULT_TIMEOUT_MS = 20_000
    MAX_ATTEMPTS = 5
    RETRY_DELAY_SEC = 2

    def __init__(self, page: Page):
        self.page = page

    def is_element_found(self, selector: str) -> bool:
        try:
            return self.page.locator(selector).is_visible(timeout=self.DEFAULT_TIMEOUT_MS)
        except PlaywrightTimeoutError:
            return False
        except Exception:
            return False

    def wait_for_element_visibility(self, selector: str) -> bool:
        visible = False
        for attempt in range(self.MAX_ATTEMPTS):
            if attempt > 0:
                time.sleep(self.RETRY_DELAY_SEC)
            try:
                if self.is_element_found(selector):
                    visible = True
                    break
            except Exception:
                pass
        return visible

    def click(self, selector: str) -> None:
        def do_click():
            self.page.locator(selector).click(timeout=self.DEFAULT_TIMEOUT_MS)

        clicked = False
        last_error = None
        for attempt in range(self.MAX_ATTEMPTS):
            if attempt > 0:
                time.sleep(self.RETRY_DELAY_SEC)
            try:
                if self.is_element_found(selector):
                    do_click()
                    clicked = True
                    break
            except Exception as e:
                last_error = e

        if not clicked and last_error:
            raise AssertionError(
                f"Failed to click {selector} after {self.MAX_ATTEMPTS} attempts. Last error: {last_error}"
            )
        assert clicked, f"Failed to click {selector} after {self.MAX_ATTEMPTS} attempts"

    def fill_text(self, selector: str, text: str) -> None:
        filled = False
        last_error = None
        for attempt in range(self.MAX_ATTEMPTS):
            if attempt > 0:
                time.sleep(self.RETRY_DELAY_SEC)
            try:
                if self.is_element_found(selector):
                    self.page.locator(selector).fill(text, timeout=self.DEFAULT_TIMEOUT_MS)
                    filled = True
                    break
            except Exception as e:
                last_error = e

        if not filled and last_error:
            raise AssertionError(
                f"Failed to fill {selector} after {self.MAX_ATTEMPTS} attempts. Last error: {last_error}"
            )
        assert filled, f"Failed to fill {selector} after {self.MAX_ATTEMPTS} attempts"

    def switch_to_frame(self, frame_selector: str):
        return self.page.frame_locator(frame_selector)

    def is_displayed(self, selector: str) -> bool:
        return self.is_element_found(selector)

    def is_element_display_with_retry(self, selector: str) -> bool:
        return self.wait_for_element_visibility(selector)

    def alert_ok(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def get_text_from_at(self, selector: str, attribute: str) -> str | None:
        if not self.wait_for_element_visibility(selector):
            return None
        return self.page.locator(selector).get_attribute(attribute)

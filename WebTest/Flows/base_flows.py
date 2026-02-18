from enum import Enum
from playwright.sync_api import Page

from WebTest.PageObject.base_pages import BasePages


# Assuming BaseTest is defined somewhere within your project

class BaseFlows:
    def __init__(self, page):
        self.page = page

        self.base_pages = BasePages(page)

    def get_current_url(self) -> str:
        return self.page.url

    def navigate_to_url(self, url: str):
        self.page.goto(url)

    def open_sidebar_menu(self, SideBarEnum: SideBar):
        self.base_pages.ClickOnMainMenueTitleByName(SideBarEnum.value)
        return self

class SideBar(Enum):
    GENERAL = "General"
    DATA_MODULE = "data module"
    WORKFLOW_MANAGEMENT = "WORKFLOW MANAGEMENT"
    AUTORIZATION_MANAGER = "AUTORIZATION MANAGER"
    API_MANAGER = "Api Manager"
    SCANOVATE_ADMIN = "SCANOVATE ADMIN"


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

    def open_main_menue_side_bar(self, SideBarEnum: SideBarMenue):
        self.base_pages.ClickOnMainMenueTitleByName(SideBarEnum.value)
        return self
    def open_sub_menue_side_bar(self, SubMenuesList: SubMenuesList):
        self.base_pages.ClickOnSubMenueTitleByName(SubMenuesList.value)
        return self

class SideBarMenue(Enum):
    GENERAL = "General"
    DATA_MODULE = "data module"
    WORKFLOW_MANAGEMENT = "WORKFLOW MANAGEMENT"
    AUTORIZATION_MANAGER = "AUTORIZATION MANAGER"
    API_MANAGER = "Api Manager"
    SCANOVATE_ADMIN = "SCANOVATE ADMIN"

class SubMenuesList(Enum):
    EMAIL_TEMPLATE = "Email Template"
    USER_EXPERIENCE_SETTINGS = "User Experience Settings"
    DASHBOARDS = "Dashboards"
    TRANSLATION_DICTIONARY = "Translation Dictionary"
    #DataModuleSubMenu
    ENTITIES_MANAGER = "Entities Manager"
    DATA_MAPPER = "Data Mapper"
    DOCUMENTS_MANAGER = "Documents Manager"
    SERVICES_MARKETPLACE = "Services Marketplace"
    #WorlkflowManagementSubMenu
    WORKFLOW_BUILDER = "Workflow Builder"
    TRIGGERS = "Triggers"
    MOBILE_FORMS = "Mobile Forms"
    MOBILE_INTERACTION = "Mobile Interaction"



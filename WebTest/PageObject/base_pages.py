from WebTest.WebInfra.web_locatore_function import WeblocatoreFunction


class BasePages(WeblocatoreFunction):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def ClickOnMainMenueTitleByName(self, title_name: str):
        selector = f"//button[normalize-space()='{title_name}']"
        self.click(selector)
        return self
    
    def ClickOnSubMenueTitleByName(self, title_name: str):
        selector = f"//div[normalize-space()='{title_name}']"
        self.click(selector)
        return self

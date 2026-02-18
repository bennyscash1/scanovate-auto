from WebTest.WebInfra.web_locatore_function import WeblocatoreFunction


class BasePages(WeblocatoreFunction):
    def __init__(self, page):
        super().__init__(page)
        self.page = page


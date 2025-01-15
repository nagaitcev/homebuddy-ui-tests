from selenium.webdriver import Chrome


class UIDriver:
    def __init__(self, page=None):
        self.page = page

    def set_page(self, current_page):
        self.page = current_page

    def get_page(self):
        try:
            return self.page
        except AttributeError:
            return None


class ChromeDriver(Chrome, UIDriver):
    pass

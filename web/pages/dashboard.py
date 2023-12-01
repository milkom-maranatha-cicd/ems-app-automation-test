from selenium.webdriver.common.by import By

from web.driver import WebDriver
from web.utils import visibility_of_element_located


class DashboardPage:

    def __init__(self, wd: WebDriver) -> None:
        self.wd = wd
        self.driver = wd.driver
        self.root_container = visibility_of_element_located(self.driver, By.ID, 'root')

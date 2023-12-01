
from web.driver import WebDriver


class SignInPage:
    URL = 'http://localhost:3000/'

    def __init__(self) -> None:
        self.driver = WebDriver().driver

    def login(self, username: str, password: str):
        self.driver.get(SignInPage.URL)

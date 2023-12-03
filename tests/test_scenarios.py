
from unittest import TestCase

from settings import APP_URL
from web.driver import WebDriver
from web.pages import SignInPage


class TestScenarios(TestCase):
    """
    Automation testing for any scenario
    within the Employee System Managemenet Software.
    """

    @classmethod
    def setUpClass(cls):
        cls.wd = WebDriver()
        cls.wd.driver.get(APP_URL)

    def test_scenario_001(self) -> None:
        """
        Automation testing scenario for:
        - Login with valid credentials,
        - Fetch a list of employees, and
        - Logout from the system.
        """
        sign_in_page = SignInPage(self.wd)

        try:
            sign_in_page.assert_properties()
        except ValueError as err:
            self.fail(f'Sign In Page Assertion Failed: {str(err)}')

        sign_in_page.run_login('admin@mail.com', 'Test@12345')

    @classmethod
    def tearDownClass(cls):
        cls.wd.driver.close()

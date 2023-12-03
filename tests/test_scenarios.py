import time

from unittest import TestCase

from web.driver import WebDriver
from web.pages import (
    DashboardPage,
    SignInPage,
)

from settings import APP_URL
from tests.data.employees import PREDEFINED_DATA


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
        - Validates employee dataset, and
        - Logout from the system.
        """
        # Open the sign in page
        sign_in_page = SignInPage(self.wd)

        # Assert properties of the sign in page
        # i.e. (page title, labels, and text buttons)
        try:
            sign_in_page.assert_properties()
        except ValueError as err:
            self.fail(f'Sign In Page Assertion Failed: {str(err)}')

        # Login with valid credentials
        dashboard_page: DashboardPage = sign_in_page.run_login(
            username='admin@mail.com',
            password='Test@12345'
        )

        # Assert properties of the dashboard page
        # i.e. (page title, labels, and text buttons)
        try:
            dashboard_page.assert_properties()
        except ValueError as err:
            self.fail(f'Dashboard Page Assertion Failed: {str(err)}')

        # Scrolls down/up to see dataset of the table employee
        # (if needed)
        if len(dashboard_page.table_dataset) >= 10:
            dashboard_page.scroll_down()
            dashboard_page.scroll_up()

        # Assert table headers
        try:
            dashboard_page.assert_table_headers()
        except ValueError as err:
            self.fail(f'Dashboard Page Assertion Failed: {str(err)}')

        # Assert table content if empty
        if len(dashboard_page.table_dataset) == 0:
            try:
                dashboard_page.assert_table_data_is_empty()
            except ValueError as err:
                self.fail(f'Dashboard Page Assertion Failed: {str(err)}')

        # Assert dataset of the table employee
        else:
            actual_data = dashboard_page.table_dataset
            expected_data = PREDEFINED_DATA
            self.assertCountEqual(actual_data, expected_data)

        # Logout from the system
        sign_in_page = dashboard_page.run_logout()
        time.sleep(1)

        # Ensure sign page is loaded with correct properties
        try:
            sign_in_page.assert_properties()
        except ValueError as err:
            self.fail(f'Sign In Page Assertion Failed: {str(err)}')

    @classmethod
    def tearDownClass(cls):
        cls.wd.driver.close()

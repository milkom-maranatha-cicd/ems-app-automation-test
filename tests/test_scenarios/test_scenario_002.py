import time

from unittest import TestCase

from web.driver import WebDriver
from web.pages import (
    AddEmployeePage,
    DashboardPage,
    SignInPage,
)

from settings import APP_URL
from tests.data.employees import PREDEFINED_DATA


class TestScenario002(TestCase):
    """
    Automation testing scenario for:
    - Login with valid credentials,
    - Validates initial state of the employee dataset,
    - Add new employee,
    - Validates updated state of the employee dataset, and
    - Logout from the system.
    """

    def setUp(self) -> None:
        self.wd = WebDriver()
        self.wd.driver.get(APP_URL)

    def test_login_add_employee_logout(self):
        """
        Run automation testing for Scenario 002
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

        # Assert initial state of the table dataset
        # Validates if table content is empty
        if len(dashboard_page.table_dataset) == 0:
            try:
                dashboard_page.assert_table_data_is_empty()
            except ValueError as err:
                self.fail(f'Dashboard Page Assertion Failed: {str(err)}')

        # Otherwise, validates dataset of the table employee
        else:
            actual_data = dashboard_page.table_dataset
            expected_data = PREDEFINED_DATA
            self.assertCountEqual(actual_data, expected_data)

        # Open add employee page
        add_employee_page: AddEmployeePage = dashboard_page.run_add_data()

        # Assert properties of the add employee page
        # i.e. (page title, labels, and text buttons)
        try:
            add_employee_page.assert_properties()
        except ValueError as err:
            self.fail(f'Add Employee Page Assertion Failed: {str(err)}')

        # Save new employee
        new_employee = {
            'first_name': 'Added',
            'last_name': 'New Employee',
            'email': 'new@employee.com',
            'salary': '20000',
            'date': '05/12/2023'
        }
        dashboard_page: DashboardPage = add_employee_page.run_add_employee(new_employee)
        time.sleep(1)

        # Scrolls down/up to see dataset of the table employee
        # (if needed)
        table_dataset_size = len(dashboard_page.table_dataset)
        if table_dataset_size >= 10:
            dashboard_page.scroll_down()

        # Assert table data contains new employee
        # Validates updated state of the table employee
        try:
            dashboard_page.assert_table_data_contains(new_employee)
        except LookupError as err:
            self.fail(f'Dashboard Page Assertion Failed: {str(err)}')

        # Logout from the system
        time.sleep(1)
        sign_in_page: SignInPage = dashboard_page.run_logout()
        time.sleep(1)

        # Ensure sign page is loaded with correct properties
        try:
            sign_in_page.assert_properties()
        except ValueError as err:
            self.fail(f'Sign In Page Assertion Failed: {str(err)}')

    def tearDown(self) -> None:
        self.wd.driver.close()

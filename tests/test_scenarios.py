import time

from dateutil.parser import parse
from unittest import TestCase

from web.driver import WebDriver
from web.pages import (
    AddEmployeePage,
    DashboardPage,
    EditEmployeePage,
    SignInPage,
)

from settings import APP_URL
from tests.data.employees import PREDEFINED_DATA


class TestScenarios(TestCase):
    """
    Automation testing for any scenario
    within the Employee System Managemenet Software.
    """

    def setUp(self) -> None:
        self.wd = WebDriver()
        self.wd.driver.get(APP_URL)

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

    def test_scenario_002(self):
        """
        Automation testing scenario for:
        - Login with valid credentials,
        - Validates initial state of the employee dataset,
        - Add new employee,
        - Validates updated state of the employee dataset, and
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
        dashboard_page.btn_add.click()

        add_employee_page = AddEmployeePage(self.wd)
        add_employee_page.assert_properties()

        # Add new employee
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

    def test_scenario_003(self):
        """
        Automation testing scenario for:
        - Login with valid credentials,
        - Validates initial state of the employee dataset,
        - Edit the first employee,
        - Validates updated state of the employee dataset, and
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

        # Select to be edited employee
        row_number = 1

        to_be_edited = dashboard_page.table_dataset[row_number - 1]
        to_be_edited['salary'] = self._to_raw_salary(to_be_edited['salary'])
        to_be_edited['date'] = self._to_date_first(to_be_edited['date'])

        # Open edit employee page
        dashboard_page.run_edit_data(row_number=row_number)
        edit_employee_page = EditEmployeePage(self.wd)
        edit_employee_page.assert_properties()

        # Edit employee
        employee = {**to_be_edited}
        employee['last_name'] = 'Edited'
        employee['email'] = 'susan-edited@mail.com'

        dashboard_page: DashboardPage = edit_employee_page.run_edit_employee(employee)
        time.sleep(1)

        # Scrolls down/up to see dataset of the table employee
        # (if needed)
        table_dataset_size = len(dashboard_page.table_dataset)
        if table_dataset_size >= 10:
            dashboard_page.scroll_down()

        # Assert table data contains updated employee
        # Validates updated state of the table employee
        try:
            dashboard_page.assert_table_data_contains(employee)
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

    def test_scenario_004(self):
        """
        Automation testing scenario for:
        - Login with valid credentials,
        - Validates initial state of the employee dataset,
        - Delete employee,
        - Validates updated state of the employee dataset, and
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

        # Delete the first employee
        row_number = 1

        deleted_data = dashboard_page.run_delete_data(row_number=row_number)
        deleted_data['salary'] = self._to_raw_salary(deleted_data['salary'])
        deleted_data['date'] = self._to_date_first(deleted_data['date'])

        # Scrolls down/up to see dataset of the table employee
        # (if needed)
        table_dataset_size = len(dashboard_page.table_dataset)
        if table_dataset_size >= 10:
            dashboard_page.scroll_down()

        # Assert table data must not contains the deleted data
        self.assertRaises(
            LookupError,
            dashboard_page.assert_table_data_contains,
            deleted_data
        )

        # Logout from the system
        time.sleep(1)
        sign_in_page: SignInPage = dashboard_page.run_logout()
        time.sleep(1)

        # Ensure sign page is loaded with correct properties
        try:
            sign_in_page.assert_properties()
        except ValueError as err:
            self.fail(f'Sign In Page Assertion Failed: {str(err)}')

    def _to_raw_salary(self, salary: str) -> str:
        return salary.replace('$', '').replace(',', '').replace('.', ',')

    def _to_date_first(self, str_date: str) -> str:
        return parse(str_date, yearfirst=True).strftime('%d/%m/%Y')

    def tearDown(self) -> None:
        self.wd.driver.close()

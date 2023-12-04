import time

from dateutil.parser import parse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict, List, Tuple

from web.converters import (
    to_date_first,
    usd_salary_to_number,
)
from web.driver import WebDriver
from web.modals.basic import BasicModal
from web.modals.confirmation import ConfirmationModal
from web.utils import (
    visibility_of_element_located,
    visibility_of_all_elements_located
)


class DashboardPage:

    def __init__(self, wd: WebDriver) -> None:
        self.wd = wd
        self.driver = wd.driver

    @property
    def container(self) -> WebElement:
        """
        Returns container of the dashboard page.
        """
        return visibility_of_element_located(
            self.driver, By.ID, 'root'
        )

    @property
    def label_title(self) -> str:
        """
        Returns label of the title of the dashboard page.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/header/h1'
        ).text

    @property
    def label_btn_add(self) -> str:
        """
        Returns label of the add employee button.
        """
        return self.btn_add.text

    @property
    def btn_add(self) -> WebElement:
        """
        Returns button add employee.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/header/div/button[1]'
        )

    @property
    def label_btn_logout(self) -> str:
        """
        Returns label of the logout button.
        """
        return self.btn_logout.text

    @property
    def btn_logout(self) -> WebElement:
        """
        Returns button logout.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/header/div/button[2]'
        )

    @property
    def tabel_headers(self) -> List[str]:
        """
        Returns the table's header of the list of employees.
        """
        headers = visibility_of_all_elements_located(
            self.driver, By.XPATH, '//*[@id="root"]/div/div/table/thead/tr/th'
        )
        return [header.text for header in headers]

    @property
    def tabel_rows(self) -> List[WebElement]:
        """
        Returns a list of row elements from the table employee.
        """
        return visibility_of_all_elements_located(
            self.driver, By.XPATH, '//*[@id="root"]/div/div/table/tbody/tr'
        )

    @property
    def table_dataset(self) -> List[Dict]:
        """
        Returns Python dataset of the table employee.
        """
        if self._is_table_empty():
            return []

        return [
            {
                'no': r.find_element(By.XPATH, './/td[1]').text,
                'first_name': r.find_element(By.XPATH, './/td[2]').text,
                'last_name': r.find_element(By.XPATH, './/td[3]').text,
                'email': r.find_element(By.XPATH, './/td[4]').text,
                'salary': r.find_element(By.XPATH, './/td[5]').text,
                'date': r.find_element(By.XPATH, './/td[6]').text
            }
            for r in self.tabel_rows
        ]

    def assert_properties(self) -> None:
        """
        Assert dashboard page properties.
        """
        print('\n> Assert dashboard page title...')
        if self.label_title != 'Employee Management Software':
            raise ValueError('Incorrect page\'s title.')

        print('> Assert label of add employee button...')
        if self.label_btn_add != 'Add Employee':
            raise ValueError('Incorrect label for the add employee button.')

        print('> Assert label of logout button...')
        if self.label_btn_logout != 'Logout':
            raise ValueError('Incorrect label for the logout button.')

    def assert_table_headers(self) -> None:
        """
        Assert content of the table employee's headers.
        """
        print('\n> Assert header of the table employee...')
        if self.tabel_headers != [
            'No.', 'First Name', 'Last Name',
            'Email', 'Salary', 'Date', 'Actions'
        ]:
            raise ValueError('Incorrect header of the table employee.')

    def assert_table_data_is_empty(self) -> None:
        """
        Assert content of the table employee is empty.
        """
        print('\n> Assert content of the table employee when its empty...')
        if not self._is_table_empty():
            raise ValueError('Table employee is not empty.')

        empty_text = self.tabel_rows[0]\
            .find_element(By.XPATH, './/td[1]').text

        if empty_text != 'No Employees':
            raise ValueError('Incorrect label for no-data employee.')

    def assert_table_data_contains(
        self,
        expected_data: Dict = {}
    ) -> None:
        """
        Assert content of the table employee.\n
        The expected data of employee must follows this format:
        ```
        {
            'first_name': <str>,
            'last_name': <str>,
            'email': <str>,
            'salary': <str>,
            'date': <str>
        }
        ```
        """
        print('\n> Assert content of the table employee contains some data...')
        if not expected_data:
            raise ValueError('Expected data can\'t be empty or none.')

        # Convert expected salary into USD
        expected_salary = float(expected_data['salary'])
        if expected_salary.is_integer():
            str_expected_salary = '${:,.0f}'.format(expected_salary)
        else:
            str_expected_salary = '${:,.2f}'.format(expected_salary)

        # Convert date format into `YYYY-MM-DD`
        expected_date = parse(expected_data['date'], dayfirst=True)\
            .strftime('%Y-%m-%d')

        # Find expected data within the list
        for item in self.table_dataset:
            if bool(
                item['first_name'] == expected_data['first_name'] and
                item['last_name'] == expected_data['last_name'] and
                item['email'] == expected_data['email'] and
                item['salary'] == str_expected_salary and
                item['date'] == expected_date
            ):
                return

        raise LookupError('Expected data is not found.')

    def scroll_up(self) -> None:
        """
        Wait for one second and then scroll up to the start of page.
        """
        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, 0)"
        )

    def scroll_down(self) -> None:
        """
        Wait for one second and then scroll down to the end of page.
        """
        time.sleep(1)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def run_logout(self) -> any:
        """
        Login to the Employee Management System app
        with valid credential.

        This method returns the sign in page instance.
        """
        from web.pages import SignInPage

        print('\n> Signing out from the system...')
        self.btn_logout.click()

        print('> Confirming sign out...')
        modal = ConfirmationModal(self.wd)
        time.sleep(1)
        modal.btn_confirm.click()

        print('> Sign out success. Redirecting to the sign in page...')
        # Wait approximately for one second (until animation is completed)
        # And then redirect to sign in page
        time.sleep(1)
        return SignInPage(self.wd)

    def run_add_data(self) -> any:
        """
        Add new employee data.

        This method returns the add new employee page instance.
        """
        from web.pages import AddEmployeePage

        self.btn_add.click()

        print('> Redirecting to the add new employee page...')
        return AddEmployeePage(self.wd)

    def run_edit_data(self, row_number: int) -> Tuple:
        """
        Edit data on the specific row number.

        This method returns a tuple of (selected employee, edit employee page)
        """
        from web.pages import EditEmployeePage

        print(f'\n> Selecting employee on row number: {row_number}...')
        dataset_size = len(self.table_dataset)
        if row_number < 1 or row_number > dataset_size:
            raise ValueError('Invalid row number.')

        to_be_edited = self.table_dataset[row_number - 1]
        to_be_edited['date'] = to_date_first(to_be_edited['date'])
        to_be_edited['salary'] = usd_salary_to_number(to_be_edited['salary'])

        print(f'> Calls edit button on row number: {row_number}...')
        row = self.tabel_rows[row_number - 1]
        btn_edit = row.find_element(By.XPATH, './/td[7]/button')
        btn_edit.click()

        # Wait approximately for one second (until animation is completed)
        # And then redirect to edit employee page
        print('> Redirecting to the edit employee page...')
        time.sleep(1)
        return (to_be_edited, EditEmployeePage(self.wd))

    def run_delete_data(self, row_number: int) -> Dict:
        """
        Delete data on the specific row number and
        returns the deleted data.

        This method returns the deleted employee.
        """
        print(f'\n> Selecting employee on row number: {row_number}...')
        dataset_size = len(self.table_dataset)
        if row_number < 1 or row_number > dataset_size:
            raise ValueError('Invalid row number.')

        to_be_deleted = self.table_dataset[row_number - 1]

        print(f'> Calls delete button on row number: {row_number}...')
        row = self.tabel_rows[row_number - 1]
        btn_delete = row.find_element(By.XPATH, './/td[8]/button')
        btn_delete.click()

        print('> Confirming action delete employee...')
        modal = ConfirmationModal(self.wd)
        time.sleep(1)
        modal.btn_confirm.click()

        print('> Check delete response...')
        if not self._is_delete_success():
            raise ValueError(
                f'Row number {row_number} can\'t be deleted!'
            )

        # Wait approximately for one second (until animation is completed)
        print(f'> Employee on row {row} is deleted.')
        time.sleep(1)
        return to_be_deleted

    def _is_table_empty(self) -> bool:
        """
        Returns `True` if the table is empty.
        """
        try:
            self.container.find_element(By.XPATH, '//*[@id="empty-row"]')
        except NoSuchElementException:
            return False

        return True

    def _is_delete_success(self) -> bool:
        """
        Returns `True` if login is success.
        """
        modal = BasicModal(self.wd)
        return bool(
            modal.label_title == 'Deleted!'
        )

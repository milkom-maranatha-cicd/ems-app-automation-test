import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Dict

from web.driver import WebDriver
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
        if self.label_title != 'Employee Management Software':
            raise ValueError('Incorrect page\'s title.')

        if self.label_btn_add != 'Add Employee':
            raise ValueError('Incorrect label for the add employee button.')

        if self.label_btn_logout != 'Logout':
            raise ValueError('Incorrect label for the logout button.')

    def assert_table_headers(self) -> None:
        """
        Assert content of the table employee's headers.
        """
        if self.tabel_headers != [
            'No.', 'First Name', 'Last Name',
            'Email', 'Salary', 'Date', 'Actions'
        ]:
            raise ValueError('Incorrect header of the table employee.')

    def assert_table_data_is_empty(self) -> None:
        """
        Assert content of the table employee is empty.
        """
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
        if not expected_data:
            raise ValueError('Expected data can\'t be empty or none.')

        for item in self.table_dataset:
            if bool(
                item['first_name'] == expected_data['first_name'] and
                item['last_name'] == expected_data['last_name'] and
                item['email'] == expected_data['email'] and
                item['salary'] == expected_data['salary'] and
                item['date'] == expected_data['date']
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
        """
        from web.pages import SignInPage

        # Open logout confirmation modal
        self.btn_logout.click()

        # Confirms logout
        modal = ConfirmationModal(self.wd)
        time.sleep(1)
        modal.btn_confirm.click()

        # Wait approximately for one second (until animation is completed)
        # And then redirect to dashboard page
        time.sleep(1)
        return SignInPage(self.wd)

    def _is_table_empty(self) -> bool:
        """
        Returns `True` if the table is empty.
        """
        try:
            self.container.find_element(By.XPATH, '//*[@id="empty-row"]')
        except NoSuchElementException:
            return False

        return True

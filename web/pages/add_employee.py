import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict

from web.driver import WebDriver
from web.modals.basic import BasicModal
from web.pages.form_employee import FormEmployee


class AddEmployeePage(FormEmployee):

    def __init__(self, wd: WebDriver) -> None:
        super().__init__(wd)

    @property
    def label_btn_add(self) -> str:
        """
        Returns label of the button add.
        """
        # Text is obtained by using the `.get_attribute` method
        # due to the type of login button is HTML input element
        return self.btn_add.get_attribute('value')

    @property
    def btn_add(self) -> WebElement:
        """
        Returns button add.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/div/input[1]'
        )

    @property
    def label_btn_cancel(self) -> str:
        """
        Returns label of the button cancel.
        """
        # Text is obtained by using the `.get_attribute` method
        # due to the type of login button is HTML input element
        return self.btn_cancel.get_attribute('value')

    @property
    def btn_cancel(self) -> WebElement:
        """
        Returns button cancel.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/div/input[2]'
        )

    def assert_properties(self) -> None:
        """
        Assert add employee page properties.
        """
        if self.label_title != 'Add Employee':
            raise ValueError("Incorrect page's title.")

        if self.label_btn_add != 'Add':
            raise ValueError('Incorrect label for the add button.')

        if self.label_btn_cancel != 'Cancel':
            raise ValueError('Incorrect label for the cancel button.')

        super().assert_properties()

    def run_add_employee(self, data: Dict = {}) -> any:
        """
        Add a new employee with valid data.\n
        The incoming data of the new employee must follows this format:
        ```
        {
            'first_name': <str>,
            'last_name': <str>,
            'email': <str>,
            'salary': <str>,
            'date': <str>
        }
        """
        from web.pages import DashboardPage

        # Fills the new employee form
        self.input_first_name.send_keys(data['first_name'])
        self.input_last_name.send_keys(data['last_name'])
        self.input_email.send_keys(data['email'])
        self.input_salary.send_keys(data['salary'])
        self.input_date.send_keys(data['date'])

        # Save data
        time.sleep(1)
        self.btn_add.click()

        # Check response message
        if not self._is_add_success():
            raise ValueError(
                'Employee data is invalid!'
            )

        # Wait approximately for one second (until animation is completed)
        # And then redirect to dashboard page
        time.sleep(1)
        return DashboardPage(self.wd)

    def run_cancel(self) -> any:
        """
        Cancel operation to add a new employee.
        """
        self.btn_cancel.click()

    def _is_add_success(self) -> bool:
        """
        Returns `True` if employee data successfully added.
        """
        modal = BasicModal(self.wd)
        return bool(
            modal.label_title == 'Added!'
        )

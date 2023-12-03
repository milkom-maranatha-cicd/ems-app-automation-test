import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict

from web.driver import WebDriver
from web.modals.basic import BasicModal
from web.pages.form_employee import FormEmployee


class EditEmployeePage(FormEmployee):

    def __init__(self, wd: WebDriver) -> None:
        super().__init__(wd)

    @property
    def label_btn_edit(self) -> str:
        """
        Returns label of the button edit.
        """
        # Text is obtained by using the `.get_attribute` method
        # due to the type of login button is HTML input element
        return self.btn_edit.get_attribute('value')

    @property
    def btn_edit(self) -> WebElement:
        """
        Returns button edit.
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
        Assert edit employee page properties.
        """
        if self.label_title != 'Edit Employee':
            raise ValueError("Incorrect page's title.")

        if self.label_btn_edit != 'Update':
            raise ValueError('Incorrect label for the add button.')

        if self.label_btn_cancel != 'Cancel':
            raise ValueError('Incorrect label for the cancel button.')

        super().assert_properties()

    def run_edit_employee(self, data: Dict = {}) -> any:
        """
        Edit existing employee with valid data.\n
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

        # Fills the edit employee form
        if self.input_first_name.get_attribute('value') != data['first_name']:
            self.input_first_name.clear()
            self.input_first_name.send_keys(data['first_name'])

        if self.input_last_name.get_attribute('value') != data['last_name']:
            self.input_last_name.clear()
            self.input_last_name.send_keys(data['last_name'])

        if self.input_email.get_attribute('value') != data['email']:
            self.input_email.clear()
            self.input_email.send_keys(data['email'])

        if self.input_salary.get_attribute('value') != data['salary']:
            self.input_salary.clear()
            self.input_salary.send_keys(data['salary'])

        if self.input_date.get_attribute('value') != data['date']:
            self.input_date.clear()
            self.input_date.send_keys(data['date'])

        # Update data
        time.sleep(1)
        self.btn_edit.click()

        # Check response message
        if not self._is_edit_success():
            raise ValueError(
                'Employee data is invalid!'
            )

        # Wait approximately for one second (until animation is completed)
        # And then redirect to dashboard page
        time.sleep(1)
        return DashboardPage(self.wd)

    def run_cancel(self) -> any:
        """
        Cancel operation to edit an existing employee.
        """
        self.btn_cancel.click()

    def _is_edit_success(self) -> bool:
        """
        Returns `True` if employee data successfully edited.
        """
        modal = BasicModal(self.wd)
        return bool(
            modal.label_title == 'Updated!'
        )

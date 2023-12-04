import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict

from web.converters import to_date_first
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
        print('\n> Assert edit employee page title...')
        if self.label_title != 'Edit Employee':
            raise ValueError("Incorrect page's title.")

        print('> Assert label of the edit button...')
        if self.label_btn_edit != 'Update':
            raise ValueError('Incorrect label for the add button.')

        print('> Assert label of the cancel button...')
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

        print('\n> Filling the edit employee form...')
        inputs = [
            self.input_first_name, self.input_last_name,
            self.input_email, self.input_salary, self.input_date
        ]
        keys = ['first_name', 'last_name', 'email', 'salary', 'date']

        for input, key in zip(inputs, keys):
            # Normalized input values
            input_value = input.get_attribute('value')

            if key == 'date':
                current_value = to_date_first(input_value)
            else:
                current_value = input_value

            # Change input field value when necessary
            current_value = input.get_attribute('value')
            new_value = data[key]
            if current_value == new_value:
                continue

            input.clear()
            input.send_keys(new_value)

        print('> Updating the employee...')
        time.sleep(1)
        self.btn_edit.click()

        print('> Check update response...')
        if not self._is_edit_success():
            raise ValueError(
                'Employee data is invalid!'
            )

        # Wait approximately for one second (until animation is completed)
        # And then redirect to dashboard page
        print('> Update success. Redirecting to the dashboard page...')
        time.sleep(1)
        return DashboardPage(self.wd)

    def run_cancel(self) -> any:
        """
        Cancel operation to edit an existing employee.

        This method returns the dashboard page instance.
        """
        from web.pages import DashboardPage

        print('\n> Canceling action edit employee...')
        self.btn_cancel.click()

        # Wait approximately for one second (until animation is completed)
        # And then redirect to dashboard page
        print('> Redirecting to the dashboard page...')
        time.sleep(1)
        return DashboardPage(self.wd)

    def _is_edit_success(self) -> bool:
        """
        Returns `True` if employee data successfully edited.
        """
        modal = BasicModal(self.wd)
        return bool(
            modal.label_title == 'Updated!'
        )

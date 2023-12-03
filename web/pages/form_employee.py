from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from web.driver import WebDriver
from web.utils import visibility_of_element_located


class FormEmployee:

    def __init__(self, wd: WebDriver) -> None:
        self.wd = wd
        self.driver = wd.driver

    @property
    def container(self) -> WebElement:
        """
        Returns container of the add employee page.
        """
        return visibility_of_element_located(
            self.driver, By.ID, 'root'
        )

    @property
    def label_title(self) -> str:
        """
        Returns label of the title of the add employee page.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/h1'
        ).text

    @property
    def label_first_name(self) -> str:
        """
        Returns label of the first name input field.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/label[1]'
        ).text

    @property
    def input_first_name(self) -> WebElement:
        """
        Returns first name input field.
        """
        return self.container.find_element(By.ID, 'firstName')

    @property
    def label_last_name(self) -> str:
        """
        Returns label of the last name input field.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/label[2]'
        ).text

    @property
    def input_last_name(self) -> WebElement:
        """
        Returns last name input field.
        """
        return self.container.find_element(By.ID, 'lastName')

    @property
    def label_email(self) -> str:
        """
        Returns label of the email input field.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/label[3]'
        ).text

    @property
    def input_email(self) -> WebElement:
        """
        Returns email input field.
        """
        return self.container.find_element(By.ID, 'email')

    @property
    def label_salary(self) -> str:
        """
        Returns label of the salary input field.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/label[4]'
        ).text

    @property
    def input_salary(self) -> WebElement:
        """
        Returns salary input field.
        """
        return self.container.find_element(By.ID, 'salary')

    @property
    def label_date(self) -> str:
        """
        Returns label of the date input field.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/div/form/label[5]'
        ).text

    @property
    def input_date(self) -> WebElement:
        """
        Returns date input field.
        """
        return self.container.find_element(By.ID, 'date')

    def assert_properties(self) -> None:
        """
        Assert add employee page properties.
        """
        if self.label_first_name != 'First Name':
            raise ValueError('Incorrect label for the first name input field.')

        if self.label_last_name != 'Last Name':
            raise ValueError('Incorrect label for the last name input field.')

        if self.label_email != 'Email':
            raise ValueError('Incorrect label for the email input field.')

        if self.label_salary != 'Salary ($)':
            raise ValueError('Incorrect label for the salary input field.')

        if self.label_date != 'Date':
            raise ValueError('Incorrect label for the date input field.')

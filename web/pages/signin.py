
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from web.driver import WebDriver
from web.modals.basic import BasicModal
from web.pages import DashboardPage
from web.utils import visibility_of_element_located


class SignInPage:

    def __init__(self, wd: WebDriver) -> None:
        self.wd = wd
        self.driver = wd.driver

    @property
    def container(self) -> WebElement:
        """
        Returns container of the sign in page.
        """
        return visibility_of_element_located(
            self.driver, By.ID, 'root'
        )

    @property
    def label_title(self) -> str:
        """
        Returns label of the title of the sign in page.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/h1'
        ).text

    @property
    def label_email(self) -> str:
        """
        Returns label of the email input field.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/label[1]'
        ).text

    @property
    def input_email(self) -> WebElement:
        """
        Returns email input field.
        """
        return self.container.find_element(By.ID, 'email')

    @property
    def label_password(self) -> str:
        """
        Returns label of the password input field.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/label[2]'
        ).text

    @property
    def input_password(self) -> WebElement:
        """
        Returns password input field.
        """
        return self.container.find_element(By.ID, 'password')

    @property
    def label_btn_login(self) -> str:
        """
        Returns label of the button login.
        """
        return self.btn_login.get_attribute('value')

    @property
    def btn_login(self) -> WebElement:
        """
        Returns button login.
        """
        return self.container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/input[3]'
        )

    def assert_properties(self) -> None:
        """
        Assert sign in page properties.
        """
        if self.label_title != 'Admin Login':
            raise ValueError("Incorrect page's title.")

        if self.label_email != 'Email':
            raise ValueError('Incorrect label for the email input field.')

        if self.label_password != 'Password':
            raise ValueError('Incorrect label for the password input field.')

        if self.label_btn_login != 'Login':
            raise ValueError('Incorrect label for the login button.')

    def run_login(self, username: str, password: str) -> DashboardPage:
        """
        Login to the Employee Management System app
        with valid credential.
        """
        # Login scenario
        self.input_email.send_keys(username)
        self.input_password.send_keys(password)
        self.btn_login.click()

        # Check response message
        if not self._is_login_success():
            raise PermissionError(
                'Unable to open dashboard page. Login failed!'
            )

        # Redirect to dashboard page
        return DashboardPage(self.wd)

    def _is_login_success(self):
        """
        Returns `True` if login is success.
        """
        modal = BasicModal(self.wd)
        return bool(
            modal.label_title == 'Successfully logged in!'
        )

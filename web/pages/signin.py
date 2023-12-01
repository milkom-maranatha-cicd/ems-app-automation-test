
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from web.driver import WebDriver
from web.utils import visibility_of_element_located


class SignInPage:

    def __init__(self, wd: WebDriver) -> None:
        self.wd = wd
        self.driver = wd.driver
        self.root_container = self.driver.find_element(By.ID, 'root')

    def login(self, username: str, password: str):
        """
        Login to the Employee Management System app
        with valid credential.
        """
        # Login functionality
        input_email = self.get_input_email()
        input_email.send_keys(username)

        input_password = self.get_input_password()
        input_password.send_keys(password)

        btn_login = self.get_btn_login()
        btn_login.click()

        # Assert response message
        message = visibility_of_element_located(
            self.driver, By.ID, 'swal2-title'
        )

        if message.text != 'Successfully logged in!':
            print('Login failed...')
            self.driver.close()

        print('Login success...')

        # Redirect to dashboard page
        from web.pages import DashboardPage
        return DashboardPage(self.wd)

    def get_label_title(self) -> str:
        """
        Returns the title of the sign in page.
        """
        return self.root_container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/h1'
        ).text

    def get_label_email(self) -> str:
        """
        Returns the label of email input field.
        """
        return self.root_container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/label[1]'
        ).text

    def get_input_email(self) -> WebElement:
        """
        Returns email input field.
        """
        return self.root_container.find_element(By.ID, 'email')

    def get_label_password(self):
        """
        Returns the label of password input field.
        """
        return self.root_container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/label[2]'
        ).text

    def get_input_password(self) -> WebElement:
        """
        Returns password input field.
        """
        return self.root_container.find_element(By.ID, 'password')

    def get_btn_login(self) -> WebElement:
        """
        Returns button login.
        """
        return self.root_container.find_element(
            By.XPATH, '//*[@id="root"]/div/form/input[3]'
        )

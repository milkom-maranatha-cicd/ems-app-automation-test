
from unittest import TestCase

from settings import APP_URL
from web.driver import WebDriver
from web.pages import SignInPage


class TestScenario001(TestCase):
    """
    Automation testing scenario for:
     - Login with valid credentials,
     - Fetch a list of employees, and
     - Logout from the system.
    """

    @classmethod
    def setUpClass(cls):
        cls.wd = WebDriver()
        cls.wd.driver.get(APP_URL)

    def test_scenario(self) -> None:
        sign_in_page = SignInPage(self.wd)

        self._assert_sign_page_properties(sign_in_page)

        sign_in_page.login('admin@mail.com', 'Test@12345')

    def _assert_sign_page_properties(self, sign_in_page) -> None:
        """
        Asserts Sign In Page Properties
        """
        actual__title = sign_in_page.get_label_title()
        expected__title = 'Admin Login'
        self.assertEqual(
            actual__title,
            expected__title
        )

        actual__label_email = sign_in_page.get_label_email()
        expected__label_email = 'Email'
        self.assertEqual(
            actual__label_email,
            expected__label_email
        )

        actual__label_password = sign_in_page.get_label_password()
        expected__label_password = 'Password'
        self.assertEqual(
            actual__label_password,
            expected__label_password
        )

        actual__text_login_button = sign_in_page.get_btn_login().get_attribute('value')
        expected__text_login_button = 'Login'
        self.assertEqual(
            actual__text_login_button,
            expected__text_login_button
        )

    @classmethod
    def tearDownClass(cls):
        cls.wd.driver.close()

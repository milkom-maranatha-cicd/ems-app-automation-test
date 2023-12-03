from selenium.webdriver.common.by import By

from web.driver import WebDriver
from web.utils import visibility_of_element_located


class BasicModal:

    def __init__(self, wd: WebDriver) -> None:
        self.wd = wd
        self.driver = wd.driver

    @property
    def label_title(self) -> str:
        """
        Returns label of the title of the modal.
        """
        return visibility_of_element_located(
            self.driver, By.ID, 'swal2-title'
        ).text

    @property
    def label_message(self) -> str:
        """
        Returns the modal's message.
        """
        return visibility_of_element_located(
            self.driver, By.ID, 'swal2-html-container'
        ).text

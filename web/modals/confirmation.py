from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from web.driver import WebDriver
from web.modals.basic import BasicModal
from web.utils import visibility_of_element_located


class ConfirmationModal(BasicModal):

    def __init__(self, wd: WebDriver) -> None:
        super().__init__(wd)

    @property
    def label_btn_confirm(self) -> WebElement:
        """
        Returns label of the confirmation button.
        """
        return self.btn_confirm.get_attribute('value')

    @property
    def btn_confirm(self) -> WebElement:
        """
        Returns confirmation button.
        """
        actions_container = visibility_of_element_located(
            self.driver, By.CLASS_NAME, 'swal2-actions'
        )
        return actions_container.find_element(
            By.CLASS_NAME, 'swal2-confirm'
        )

    @property
    def label_btn_cancel(self) -> WebElement:
        """
        Returns label of the cancel button.
        """
        return self.btn_cancel.get_attribute('value')

    @property
    def btn_cancel(self) -> WebElement:
        """
        Returns cancel button.
        """
        actions_container = visibility_of_element_located(
            self.driver, By.CLASS_NAME, 'swal2-actions'
        )
        return actions_container.find_element(
            By.CLASS_NAME, 'swal2-cancel'
        )

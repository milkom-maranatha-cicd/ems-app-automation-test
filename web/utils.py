from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import List, Union


def visibility_of_element_located(
    driver: Union[
        webdriver.Chrome, webdriver.Firefox, webdriver.Safari
    ],
    by: By,
    value: str,
    wait_for: int = 10,
) -> WebElement:
    """
    Wait until visibility of element with specific identifier
    is located within that `driver`.
    """
    try:
        return WebDriverWait(driver, wait_for)\
            .until(EC.visibility_of_element_located((by, value)))
    except Exception as ex:
        driver.quit()
        raise ex


def visibility_of_all_elements_located(
    driver: Union[
        webdriver.Chrome, webdriver.Firefox, webdriver.Safari
    ],
    by: By,
    value: str,
    wait_for: int = 10,
) -> List[WebElement]:
    """
    Wait until visibility of all elements with specific identifier
    are located within that `driver`.
    """
    try:
        return WebDriverWait(driver, wait_for)\
            .until(EC.visibility_of_all_elements_located((by, value)))
    except Exception as ex:
        driver.quit()
        raise ex

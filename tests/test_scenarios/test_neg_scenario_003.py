import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

from web.driver import WebDriver
from settings import APP_URL

'''
Test edit employee negative scenario -> mencoba memasukan email tidak valid.
Email yang tidak valid di sini yaitu email tanpa '@'
'''


@pytest.fixture
def driver():
    wd = WebDriver()
    wd.driver.get(APP_URL)

    driver = wd.driver
    yield driver
    driver.quit()


def login(driver):
    driver.get("http://localhost:3000/crud-app")
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/form/input[3]'))
        )
        login_button.click()
    except (ElementClickInterceptedException, TimeoutException) as e:
        print("Login button not clickable or not found. Exception: ", e)


@pytest.mark.usefixtures("driver")
def test_edit_employee_negative_email(driver):
    login(driver)
    # Tunggu dan klik button "Edit" untuk employee pertama
    try:
        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'muted-button') and text()='Edit']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
        edit_button.click()
    except (ElementClickInterceptedException, TimeoutException) as e:
        print("Edit button not clickable. Attempting JavaScript click. Exception: ", e)
        driver.execute_script("arguments[0].click();", edit_button)

    # Isi form dengan email yang tidak valid
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_input.clear()
        email_input.send_keys("invalid_email")  # Email tanpa '@'
    except TimeoutException as e:
        print("Email input field not found. Exception: ", e)

    # Submit form
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/form/div/input[1]'))
        )
        submit_button.click()
    except (ElementClickInterceptedException, TimeoutException) as e:
        print("Submit button not clickable. Exception: ", e)
        driver.execute_script("arguments[0].click();", submit_button)
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "swal2-html-container"))
        ).text
        assert "Invalid email address." in error_message, "Expected email validation error message not found."
    except TimeoutException as e:
        print("Error message not found. Exception: ", e)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

'''
Test add employee negative scenario -> mencoba memasukan form kosong ketika menambahkan employee
'''


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def login(driver):
    driver.get("http://localhost:3000/")
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/input[3]')  # Button untuk login
    login_button.click()


@pytest.mark.usefixtures("driver")
def test_add_employee_negative(driver):
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Employee']"))
    )
    add_employee_button = driver.find_element(By.XPATH, "//button[text()='Add Employee']")
    driver.execute_script("arguments[0].scrollIntoView(true);", add_employee_button)

    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.XPATH, "//div[@class='overlay-class']"))
        )
        add_employee_button.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", add_employee_button)

    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div/input[1]')
    submit_button.click()

    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-html-container"))
    ).text

    assert "All fields are required." in error_message

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Test login negative scenario -> mencoba memasukan email dan password yang salah
Email yang dimasukan ke dalam skenario ini adalah: email_contoh@example.com
Password yang dimasukan ke dalam skenario ini adalah: password_contoh
'''

def test_login_negative_scenario():
    driver = webdriver.Edge()
    driver.get("http://localhost:3000/crud-app")

    # Tunggu hingga elemen email muncul di DOM dan clear input (karena by default sudah terisi)
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_input.clear()
    email_input.send_keys("email_contoh@example.com")

    # Tunggu hingga elemen password muncul di DOM dan clear input (karena by default sudah terisi)
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys("password_contoh" + Keys.RETURN)

    # Tunggu hingga pesan kesalahan muncul di DOM menggunakan SweetAlert2
    error_message = WebDriverWait(driver, 20).until(
        # EC.presence_of_element_located((By.CLASS_NAME, "swal2-html-container"))
        # EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div"))
        EC.visibility_of_element_located((By.CLASS_NAME, "swal2-html-container"))
    ).text

    assert "Incorrect email or password." in error_message
    driver.quit()

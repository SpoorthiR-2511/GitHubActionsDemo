from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def perform_forgot_password(email):

    driver = webdriver.Chrome()

    driver.get("http://localhost:8501")

    time.sleep(3)

    inputs = driver.find_elements(
        By.XPATH,
        "//input[@type='text']"
    )

    inputs[2].send_keys(email)

    buttons = driver.find_elements(
        By.TAG_NAME,
        "button"
    )

    for button in buttons:
        if button.text == "Reset Password":
            button.click()
            break

    time.sleep(3)

    return driver

def test_registered_email():

    driver = perform_forgot_password(
        "admin@gmail.com"
    )

    assert (
        "Password Reset Confirmation Displayed"
        in driver.page_source
    )

    driver.quit()

def test_unregistered_email():

    driver = perform_forgot_password(
        "test@gmail.com"
    )

    assert (
        "Email Not Registered"
        in driver.page_source
    )

    driver.quit()

def test_invalid_email():

    driver = perform_forgot_password(
        "admingmail"
    )

    assert (
        "Invalid Email Format"
        in driver.page_source
    )

    driver.quit()

def test_empty_email():

    driver = perform_forgot_password(
        ""
    )

    assert (
        "Email Required"
        in driver.page_source
    )

    driver.quit()

def test_special_character_email():

    driver = perform_forgot_password(
        "@@@@"
    )

    assert (
        "Invalid Email"
        in driver.page_source
    )

    driver.quit()
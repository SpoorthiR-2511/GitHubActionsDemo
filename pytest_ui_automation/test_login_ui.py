from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://localhost:8501"


def perform_login(username, password):

    driver = webdriver.Chrome()

    driver.get(URL)

    time.sleep(2)

    inputs = driver.find_elements(By.TAG_NAME, "input")

    inputs[0].send_keys(username)
    inputs[1].send_keys(password)

    driver.find_element(
        By.XPATH,
        "//button[contains(.,'Login')]"
    ).click()

    time.sleep(2)

    return driver


def test_valid_login():

    driver = perform_login(
        "spoorthi@gmail.com",
        "Spoorthi@123"
    )

    assert "Home Page Displayed" in driver.page_source

    driver.quit()


def test_invalid_email_domain():

    driver = perform_login(
        "spoorthi@yahoo.com",
        "Spoorthi@123"
    )

    assert "Username must end with @gmail.com" in driver.page_source

    driver.quit()


def test_empty_username():

    driver = perform_login(
        "",
        "Spoorthi@123"
    )

    assert "Username Required" in driver.page_source

    driver.quit()


def test_empty_password():

    driver = perform_login(
        "spoorthi@gmail.com",
        ""
    )

    assert "Password Required" in driver.page_source

    driver.quit()


def test_short_password():

    driver = perform_login(
        "spoorthi@gmail.com",
        "Spo@1"
    )

    assert "Password must be at least 8 characters" in driver.page_source

    driver.quit()


def test_password_without_uppercase():

    driver = perform_login(
        "spoorthi@gmail.com",
        "spoorthi@123"
    )

    assert "Password must contain an uppercase letter" in driver.page_source

    driver.quit()


def test_password_without_lowercase():

    driver = perform_login(
        "spoorthi@gmail.com",
        "SPOORTHI@123"
    )

    assert "Password must contain a lowercase letter" in driver.page_source

    driver.quit()


def test_password_without_number():

    driver = perform_login(
        "spoorthi@gmail.com",
        "Spoorthi@abc"
    )

    assert "Password must contain a number" in driver.page_source

    driver.quit()


def test_password_without_special_character():

    driver = perform_login(
        "spoorthi@gmail.com",
        "Spoorthi123"
    )

    assert "Password must contain a special character" in driver.page_source

    driver.quit()
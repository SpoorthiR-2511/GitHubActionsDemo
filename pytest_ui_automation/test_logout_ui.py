from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_logout():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(
            By.ID,
            "username"
        ).send_keys("tomsmith")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("SuperSecretPassword!")

        driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        driver.find_element(
            By.CSS_SELECTOR,
            "a.button.secondary.radius"
        ).click()

        assert (
            "You logged out of the secure area!"
            in driver.page_source
        )

    finally:
        driver.quit()

def test_logout_without_login():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        logout_buttons = driver.find_elements(
            By.CSS_SELECTOR,
            "a.button.secondary.radius"
        )

        assert len(logout_buttons) == 0

    finally:
        driver.quit()

def test_multiple_logout():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(
            By.ID,
            "username"
        ).send_keys("tomsmith")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("SuperSecretPassword!")

        driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        driver.find_element(
            By.CSS_SELECTOR,
            "a.button.secondary.radius"
        ).click()

        assert (
            "You logged out of the secure area!"
            in driver.page_source
        )

        logout_buttons = driver.find_elements(
            By.CSS_SELECTOR,
            "a.button.secondary.radius"
        )

        assert len(logout_buttons) == 0

    finally:
        driver.quit()
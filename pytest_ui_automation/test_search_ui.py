from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://localhost:8501"


def perform_search(search_value):

    driver = webdriver.Chrome()

    driver.get(URL)

    time.sleep(5)

    inputs = driver.find_elements(
        By.XPATH,
        "//input[@type='text']"
    )

    inputs[1].send_keys(search_value)

    buttons = driver.find_elements(
        By.TAG_NAME,
        "button"
    )

    for button in buttons:
        if button.text == "Search":
            button.click()
            break

    time.sleep(3)

    return driver

def test_valid_search():

    driver = perform_search("Laptop")

    assert "Products Found" in driver.page_source

    driver.quit()

def test_invalid_search():

    driver = perform_search("WashingMachine")

    assert "No Products Found" in driver.page_source

    driver.quit()

def test_empty_search():

    driver = perform_search("")

    assert "Enter Product Name" in driver.page_source

    driver.quit()

def test_special_character_search():

    driver = perform_search("@@@@")

    assert "Invalid Search Input" in driver.page_source

    driver.quit()

def test_partial_search():

    driver = perform_search("Lap")

    assert "Products Found" in driver.page_source

    driver.quit()
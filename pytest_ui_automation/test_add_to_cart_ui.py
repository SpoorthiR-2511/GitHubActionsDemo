from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://localhost:8501"


def open_app():

    driver = webdriver.Chrome()

    driver.get(URL)

    time.sleep(5)

    return driver


def select_product(driver, product_name):

    driver.find_element(
        By.XPATH,
        f"//*[contains(text(),'{product_name}')]"
    ).click()

    time.sleep(1)


def test_add_single_product():

    driver = open_app()

    try:

        select_product(driver, "Laptop")

        driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(3)

        assert "Laptop added to cart" in driver.page_source

    finally:
        driver.quit()


def test_add_multiple_products():

    driver = open_app()

    try:

        select_product(driver, "Laptop")

        driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(2)

        select_product(driver, "TV")

        driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(3)

        assert "Cart Count: 2" in driver.page_source

    finally:
        driver.quit()


def test_duplicate_product():

    driver = open_app()

    try:

        select_product(driver, "Laptop")

        driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(2)

        driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(2)

        assert "Cart Count: 2" in driver.page_source

    finally:
        driver.quit()


def test_add_after_search():

    driver = open_app()

    try:

        inputs = driver.find_elements(
            By.XPATH,
            "//input[@type='text']"
        )

        inputs[1].send_keys("Laptop")

        search_buttons = driver.find_elements(
            By.TAG_NAME,
            "button"
        )

        for btn in search_buttons:
            if btn.text == "Search":
                driver.execute_script("arguments[0].click();", btn)
                break

        time.sleep(2)

        select_product(driver, "Laptop")

        driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(2)

        assert "Laptop added to cart" in driver.page_source

    finally:
        driver.quit()


def test_add_without_selection():

    driver = open_app()

    try:

        driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(2)

        assert "Please Select Product" in driver.page_source

    finally:
        driver.quit()
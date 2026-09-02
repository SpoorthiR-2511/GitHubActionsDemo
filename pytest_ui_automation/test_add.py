from selenium import webdriver
from selenium.webdriver.common.by import By
import time


URL = "http://localhost:8501"


class AutomationPortalPage:
    def __init__(self):
        self.driver = webdriver.Chrome()

        self.driver.get(URL)

        self.driver.maximize_window()

        time.sleep(3)

    def search_product(self, product):
        inputs = self.driver.find_elements(
            By.XPATH,
            "//input[@type='text']"
        )

        inputs[1].clear()

        inputs[1].send_keys(product)

        buttons = self.driver.find_elements(
            By.TAG_NAME,
            "button"
        )

        for button in buttons:
            if button.text == "Search":
                self.driver.execute_script(
                    "arguments[0].click();",
                    button,
                )
                break

        time.sleep(2)

    def select_product(self, product_name):
        self.driver.find_element(
            By.XPATH,
            f"//*[contains(text(),'{product_name}')]"
        ).click()

        time.sleep(1)

    def add_to_cart(self):
        self.driver.find_element(
            By.XPATH,
            "//button[contains(.,'Add to Cart')]"
        ).click()

        time.sleep(2)

    def verify_product_added(self, product_name):
        expected_message = (
            f"{product_name} added to cart"
        )

        return (
            expected_message
            in self.driver.page_source
        )

    def close_browser(self):
        self.driver.quit()


def test_add_after_search():
    page = AutomationPortalPage()

    try:
        page.search_product("Laptop")

        page.select_product("Laptop")

        page.add_to_cart()

        assert page.verify_product_added(
            "Laptop"
        )

    finally:
        page.close_browser()


if __name__ == "__main__":
    page = AutomationPortalPage()

    try:
        page.search_product("Laptop")

        page.select_product("Laptop")

        page.add_to_cart()

        print(
            "Laptop added successfully"
        )

    finally:
        page.close_browser()
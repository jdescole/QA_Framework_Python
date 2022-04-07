from selenium.webdriver.common.by import By
from Src.webdriver.webdriver_tools import Browser
from Src.Locators.j_pet_store_locators import Locator


class Home:
    def __init__(self, url):
        self.driver = Browser(url).driver
        self.heading = self.driver.find_element(By.ID, Locator.heading).text
        self.enter_store = self.driver.find_element(By.XPATH, Locator.enter_store)

    def get_heading(self):
        return self.heading

    def get_enter_store(self):
        return self.enter_store

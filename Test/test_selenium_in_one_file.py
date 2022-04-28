import pytest
from selenium.webdriver.support.wait import WebDriverWait
import urllib3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestSyntellis:
    @pytest.fixture(scope="class")
    def driver(self, _headless=False):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.headless = _headless
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("https://petstore.octoperf.com/")
        yield self.driver
        self.driver.quit()

    def test_something(self, driver):
        textiti = driver.find_element(By.XPATH, '//*[@id="Content"]/h2')
        wait = WebDriverWait(driver, 10)
        wait.until(lambda driver: driver.current_url != "https://petstore.octoperf.com/")
        print(textiti)
        assert textiti == "Welcome to JPetStore 6"

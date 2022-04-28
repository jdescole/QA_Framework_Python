import urllib3
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, url, _headless=True):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_capabilities())
        self.driver.get(url)

    def chrome_capabilities(self):
        options = ChromeOptions()
        # options.add_argument("headless")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        return options

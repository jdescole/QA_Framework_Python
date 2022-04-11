import urllib3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, url, _headless=True):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.headless = _headless
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get(url)

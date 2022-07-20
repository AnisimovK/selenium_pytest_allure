import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import TestData
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    web_driver.implicitly_wait(20)
    yield
    web_driver.close()
    web_driver.quit()

# , "firefox"
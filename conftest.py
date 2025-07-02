import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    url = "https://the-internet.herokuapp.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(0.5)
    yield driver
    driver.quit()
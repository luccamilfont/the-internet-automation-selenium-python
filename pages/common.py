from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CommonOps:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        
    def click_link_by_text(self, link_value):
        link = self.driver.find_element(by=By.LINK_TEXT, value=link_value)
        link.click()
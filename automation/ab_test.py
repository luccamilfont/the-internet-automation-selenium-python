from selenium.webdriver.common.by import By
from .common import CommonOps

class ABTest(CommonOps):
    def get_header(self):
        return self.driver.find_element(by=By.TAG_NAME, value="h3")
    
    def clear_cookies_and_refresh(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
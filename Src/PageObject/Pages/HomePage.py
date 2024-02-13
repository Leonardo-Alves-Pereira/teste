import sys
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.PageObject.Locators import Locator

class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)  # Inicialize a variável 'wait' aqui
        self.driver.get("https://www.google.com/")
        # self.driver.set_page_load_timeout(0)
        self.logo = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.logo)))
        self.search_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.search_text)))
        self.submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locator.submit)))

    def getSearchText(self):
        return self.search_text

    def getSubmit(self):
        return self.submit

    def getWebPageLogo(self):
        return self.logo

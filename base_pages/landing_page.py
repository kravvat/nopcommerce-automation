from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LandingPage:
    __possible_categories = [
        "computers",
        "electronics",
        "apparel",
        "digital-downloads",
        "books",
        "jewelry",
        "gift-cards",
    ]


    def __init__(self, driver, category):
        self.driver = driver
        self.xpath = f"//div[@role='menuitem']//a[@href='/{category}']" 
        self.wait = WebDriverWait(driver, 10)


    def click_category(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.xpath))).click()

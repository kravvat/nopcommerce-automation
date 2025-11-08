from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver, product_name):
        self.driver = driver
        self.xpath = f"//div[@class='picture']/a[@href='/{product_name}']"
        self.wait = WebDriverWait(driver, 10)
        
    
    def click_product_name(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.xpath))).click()

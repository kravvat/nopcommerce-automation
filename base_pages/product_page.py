from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_wishlist_xpath = "(//button[text()='Add to wishlist'])[1]"
        self.wishlist_xpath = "(//a[@href='/wishlist'])[1]"
        self.wait = WebDriverWait(driver, 10)
        
    
    def click_add_to_wishlist(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.add_to_wishlist_xpath))).click()


    def click_wishlist(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.wishlist_xpath))).click()

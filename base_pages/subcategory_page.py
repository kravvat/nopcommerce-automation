from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubcategoryPage:
    __possible_subcategories = [
        "desktops",
        "notebooks",
        "software",
        "camera-photo",
        "ceell-phone",
        "others",
        "shoes",
        "clothing",
        "accessories",
    ]
    

    def __init__(self, driver, subcategory):
        self.driver = driver
        self.subcategory = f"//h2[@class='title']/a[@href='/{subcategory}']"
        self.wait = WebDriverWait(driver, 10)
        

    def click_subcategory(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.subcategory))).click()

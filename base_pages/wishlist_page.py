from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WishlistPage:
    def __init__(self, driver, product_name):
        self.driver = driver
        self.product_name = product_name
        self.table_rows_xpath = "//table[@class='cart']/tbody/tr"
        self.wait = WebDriverWait(driver, 10)
        
    def get_table_rows_count(self):
        return len(self.driver.find_element(By.XPATH, self.table_rows_xpath))


    def search_product(self):
        for row in range(1, self.get_table_rows_count() + 1):
            product_name_field = self.driver.find_element(By.XPATH, f"//table[@class='cart']/tbody/tr[{row}]/td[4]").text
            if self.product_name == product_name_field:
                return True

        return False

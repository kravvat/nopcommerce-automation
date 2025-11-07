from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LandingPage:
    link_computers_category_xpath = "//div[@role='menuitem']//a[@href='/computers']"
    link_electronics_category_xpath = "//div[@role='menuitem']//a[@href='/electronics']"
    link_apparel_category_xpath = "//div[@role='menuitem']//a[@href='/apparel']"
    link_digital_category_xpath = "//div[@role='menuitem']//a[@href='/digital-downloads']"
    link_books_category_xpath = "//div[@role='menuitem']//a[@href='/books']"
    link_jewelry_category_xpath = "//div[@role='menuitem']//a[@href='/jewelry']"
    link_gift_category_xpath = "//div[@role='menuitem']//a[@href='/gift-cards']"


    def __init__(self, driver, category):
        self.driver = driver
        self.category = category
        self.wait = WebDriverWait(driver, 10)

    def click_category(self):
        match self.category:
            case "computers":
                self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.link_computers_category_xpath))).click()
            case "electronics":
                self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.link_electronics_category_xpath))).click()
            case "apparel":
                self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.link_apparel_category_xpath))).click()
            case "digital":
                self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.link_digital_category_xpath))).click()
            case "books":
                self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.link_books_category_xpath))).click()
            case "jewelry":
                self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.link_jewelry_category_xpath))).click()
            case "gift":
                self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.link_gift_category_xpath))).click()

import pytest, os, time
from base_pages.admin_login_page import AdminLoginPage 
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from utilities.logger import LogMaker


class TestAdminLogin:
    admin_page_url = ReadConfig.get_admin_page_url()
    admin_username = ReadConfig.get_admin_username() 
    invalid_admin_username = ReadConfig.get_invalid_admin_username()
    admin_password = ReadConfig.get_admin_password()
    logger = LogMaker.generate_log()


    def test_title_verification(self, setup):
        self.logger.info("Starting: TestAdminLogin > test_title_verification")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        title = self.driver.title
        if title == "nopCommerce demo store. Login":
            self.logger.info("Success: Title does match")
            assert True
            self.driver.close()
        else:
            self.logger.warning("Fail: Title does not match")
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False
    

    def test_valid_admin_login(self, setup):
        self.logger.info("Starting: TestAdminLogin > test_valid_admin_login")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_login_page.enter_username(self.admin_username)
        self.admin_login_page.enter_password(self.admin_password)
        self.admin_login_page.click_login()

        dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        if dashboard_text == "Dashboard":
            self.logger.info("Success: 'Dashboard' found")
            assert True
            self.driver.close()
        else:
            self.logger.warning("Fail: 'Dashboard' not found")
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False


    def test_invalid_admin_login(self, setup):
        self.logger.info("Starting: TestAdminLogin > test_invalid_admin_login")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_login_page.enter_username(self.invalid_admin_username)
        self.admin_login_page.enter_password(self.admin_password)
        self.admin_login_page.click_login()

        error_message = self.driver.find_element(By.XPATH, "//li").text
        if error_message == "No customer account found":
            self.logger.info("Success: Invalid login detected")
            assert True
            self.driver.close()
        else:
            self.logger.warning("Fail: Invalid login worked")
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False

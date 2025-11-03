import pytest, time
from base_pages.admin_login_page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogMaker
from base_pages.search_customer_page import SearchCustomerPage
from base_pages.add_customer_page import AddCustomerPage

class TestSearchCustomer04:
    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_admin_username()
    password_admin = ReadConfig.get_admin_password()
    logger = LogMaker.generate_log()

    email = "admin@yourStore.com"
    first_name = "John"
    last_name = "Smith"
    company = ""
    

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("Starting: TestSearchCUstomer04 > test_search_customer_by_email")
        self.driver = setup
    
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password_admin)
        self.admin_login_page.click_login()
        self.logger.info("Login completed")

        time.sleep(2)
        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_customers_menu()
        time.sleep(1)
        self.add_customer.click_customers_menu_option()
        
        time.sleep(1)
        self.search_customer = SearchCustomerPage(self.driver)
        self.search_customer.enter_customer_email(self.email)
        self.search_customer.click_search_button()
        
        time.sleep(1)
        email_found = self.search_customer.search_customer_by_email(self.email)
        
        if email_found:
            assert True
            self.logger.info("Success: Customer with a given email was found")
            self.driver.close()
        else:
            self.logger.warning("Fail: Customer with a given email does not exist")
            self.driver.save_screenshot(f".\\screenshots\\test_search_customer_by_email.png")
            self.driver.close()
            assert False
    

    @pytest.mark.sanity
    def test_search_customer_by_first_name(self, setup):
        self.logger.info("Starting: TestSearchCUstomer04 > test_search_customer_by_first_name")
        self.driver = setup
    
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password_admin)
        self.admin_login_page.click_login()
        self.logger.info("Login completed")

        time.sleep(2)
        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_customers_menu()
        time.sleep(1)
        self.add_customer.click_customers_menu_option()
        
        time.sleep(1)
        self.search_customer = SearchCustomerPage(self.driver)
        self.search_customer.enter_first_name(self.first_name)
        self.search_customer.click_search_button()
        
        time.sleep(1)
        first_name_found = self.search_customer.search_customer_by_first_name(self.first_name)
        
        if first_name_found:
            assert True
            self.logger.info("Success: Customer with a given first_name was found")
            self.driver.close()
        else:
            self.logger.warning("Fail: Customer with a given first_name does not exist")
            self.driver.save_screenshot(f".\\screenshots\\test_search_customer_by_first_name.png")
            self.driver.close()
            assert False
            

    def test_search_customer_by_last_name(self, setup):
        self.logger.info("Starting: TestSearchCUstomer04 > test_search_customer_by_first_name")
        self.driver = setup
    
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password_admin)
        self.admin_login_page.click_login()
        self.logger.info("Login completed")

        time.sleep(2)
        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_customers_menu()
        time.sleep(1)
        self.add_customer.click_customers_menu_option()
        
        time.sleep(1)
        self.search_customer = SearchCustomerPage(self.driver)
        self.search_customer.enter_last_name(self.last_name)
        self.search_customer.click_search_button()
        
        time.sleep(1)
        last_name_found = self.search_customer.search_customer_by_last_name(self.last_name)
        
        if last_name_found:
            assert True
            self.logger.info("Success: Customer with a given last_name was found")
            self.driver.close()
        else:
            self.logger.warning("Fail: Customer with a given last_name does not exist")
            self.driver.save_screenshot(f".\\screenshots\\test_search_customer_by_last_name.png")
            self.driver.close()
            assert False
        

    def test_search_customer_by_company(self, setup):
        self.logger.info("Starting: TestSearchCUstomer04 > test_search_customer_by_first_name")
        self.driver = setup
    
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password_admin)
        self.admin_login_page.click_login()
        self.logger.info("Login completed")

        time.sleep(2)
        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_customers_menu()
        time.sleep(1)
        self.add_customer.click_customers_menu_option()
        
        time.sleep(1)
        self.search_customer = SearchCustomerPage(self.driver)
        self.search_customer.enter_company(self.company)
        self.search_customer.click_search_button()
        
        time.sleep(1)
        company_found = self.search_customer.search_customer_by_company(self.company)
        
        if company_found:
            assert True
            self.logger.info("Success: Customer with a given company was found")
            self.driver.close()
        else:
            self.logger.warning("Fail: Customer with a given company does not exist")
            self.driver.save_screenshot(f".\\screenshots\\test_search_customer_by_company.png")
            self.driver.close()
            assert False

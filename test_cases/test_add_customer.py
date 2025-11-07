import time, random, pytest
from base_pages.admin_login_page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogMaker
from base_pages.add_customer_page import AddCustomerPage
from utilities.generate_data import GenerateRandomData
 

class TestAddCustomer03:
    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_admin_username()
    password_admin = ReadConfig.get_admin_password()
    logger = LogMaker.generate_log()

    email = GenerateRandomData.generate_random_email()
    password_user = GenerateRandomData.generate_random_password()
    first_name = GenerateRandomData.generate_random_first_name() 
    last_name = GenerateRandomData.generate_random_last_name()
    company = GenerateRandomData.generate_random_company()
    comment = GenerateRandomData.generate_random_comment()
    
    success_message = "The new customer has been added successfully."
    

    @pytest.mark.parametrize("instance_id", range(10))
    def test_add_customer(self, setup, instance_id):
        self.logger.info(f"Starting: TestAddCustomer03 > test_add_customer | Instance #{instance_id}")
        self.driver = setup

        self.driver.maximize_window()
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password_admin)
        self.admin_login_page.click_login()
        self.logger.info(f"Login completed | Instance #{instance_id}")
        
        time.sleep(2)
        self.add_customer = AddCustomerPage(self.driver)
        self.add_customer.click_customers_menu()
        time.sleep(1)
        self.add_customer.click_customers_menu_option()
        time.sleep(1)
        self.add_customer.click_add_new()
        self.add_customer.enter_email(self.email)
        self.add_customer.enter_password(self.password_user)
        self.add_customer.enter_first_name(self.first_name)
        self.add_customer.enter_last_name(self.last_name) 
        self.add_customer.select_gender(random.choice(['male', 'female']))
        self.add_customer.enter_company(self.company)
        
        tax_exempt_randomizer = random.choice([True, False])
        if tax_exempt_randomizer:
            self.add_customer.select_tax_exempt()

        self.add_customer.select_newsletter()
        self.add_customer.select_customer_roles(
            random.choice(['registered', 'moderators', 'guests', 'vendors'])
        )
        
        vendor_randomizer = random.choice([True, False])
        if vendor_randomizer:
            self.add_customer.select_manager(
                random.choice(['Vendor 1', 'Vendor 2'])
            )
            
        active_randomizer = random.choice([True, False])
        if active_randomizer:
            self.add_customer.select_active()
            
        change_password_randomizer = random.choice([True, False])
        if change_password_randomizer:
            self.add_customer.select_must_change_password()   
        
        self.add_customer.enter_comment(self.comment)
        self.add_customer.click_save()

        if self.success_message not in self.add_customer.get_success_message() or instance_id == 7:
            self.logger.warning(f"Fail: New customer was not created | Instance #{instance_id}")
            self.driver.save_screenshot(f".\\screenshots\\test_add_customer_instance_{instance_id}.png")
            self.driver.close()
            assert False
        elif self.success_message in self.add_customer.get_success_message():
            assert True
            self.logger.info(f"Success: New customer created | Instance #{instance_id}")
            self.driver.close()

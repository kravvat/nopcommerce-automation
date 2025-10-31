import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomerPage:
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    link_customers_menu_option_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_add_new_xpath = "//a[normalize-space()='Add new']"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_first_name_id = "FirstName"
    textbox_last_name_id = "LastName"
    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"
    textbox_company_id = "Company"
    checkbox_tax_id = "IsTaxExempt"
    input_newsletter_xpath = "(//input[@role='searchbox'])[1]"
    list_option_newsletter_xpath = "//li[contains(text(), 'nopCommerce admin demo store')]"
    input_customer_roles_xpath = "(//input[@role='searchbox'])[2]" 
    list_option_customer_role_administrators_xpath = "//li[contains(text(), 'Administrators')]"
    list_option_customer_role_moderators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    list_option_customer_role_registered_xpath = "//li[contains(text(), 'Registered')]"
    list_option_customer_role_guests_xpath = "//li[contains(text(), 'Guests')]"
    list_option_customer_role_vendors_xpath = "//li[contains(text(), 'Vendors')]"
    list_option_customer_role_remove_xpath = "(//li//span[@class='select2-selection__choice__remove'])[2]"
    dropdown_manager_id = "VendorId"
    checkbox_is_active_id = "Active"
    checkbox_must_change_password_id = "MustChangePassword"
    textbox_comment_id = "AdminComment"
    button_save_xpath = "//button[@name='save']"
    success_message_xpath = "//div[@class='alert alert-success alert-dismissable']"
    
    
    def __init__(self, driver):
        self.driver = driver
        
    def click_customers_menu(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_xpath).click()
        
    def click_customers_menu_option(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_option_xpath).click()
        
    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.button_add_new_xpath).click()
        
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    
    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.textbox_first_name_id).send_keys(first_name)
        
    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.textbox_last_name_id).send_keys(last_name)

    def select_gender(self, gender):
        if gender == "male":
            self.driver.find_element(By.ID, self.radio_gender_male_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()
        
    def enter_company(self, company):
        self.driver.find_element(By.ID, self.textbox_company_id).send_keys(company)
    
    def select_tax_exempt(self):
        self.driver.find_element(By.ID, self.checkbox_tax_id).click()
    
    def select_newsletter(self):
        self.driver.find_element(By.XPATH, self.input_newsletter_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.list_option_newsletter_xpath).click()
        time.sleep(1)

    def select_customer_roles(self, role):
        if role == "registered":
            pass

        if role == "administrators":
            self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.list_option_customer_role_administrators_xpath).click()
            self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
            
        if role == "moderators":
            self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.list_option_customer_role_moderators_xpath).click()
            self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
            
        if role == "guests":
            self.driver.find_element(By.XPATH, self.list_option_customer_role_remove_xpath).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.list_option_customer_role_guests_xpath).click()
            self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
        
        if role == "vendors":
            self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.list_option_customer_role_vendors_xpath).click()
            self.driver.find_element(By.XPATH, self.input_customer_roles_xpath).click()
    
    def select_manager(self, manager):
        dropdown = Select(self.driver.find_element(By.ID, self.dropdown_manager_id))
        dropdown.select_by_visible_text(manager)

    def select_active(self):
        self.driver.find_element(By.ID, self.checkbox_is_active_id).click()
        
    def select_must_change_password(self):
        self.driver.find_element(By.ID, self.checkbox_must_change_password_id).click()
    
    def enter_comment(self, comment):
        self.driver.find_element(By.ID, self.textbox_comment_id).send_keys(comment)
   
    def click_save(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()
 
    def get_success_message(self):
        return self.driver.find_element(By.XPATH, self.success_message_xpath).text

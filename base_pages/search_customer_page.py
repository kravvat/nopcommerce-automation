from selenium.webdriver.common.by import By

class SearchCustomerPage:
    textbox_email_id = "SearchEmail"
    textbox_first_name_id = "SearchFirstName"
    textbox_last_name_id = "SearchLastName"
    textbox_company_id = "SearchCompany"
    button_search_id = "search-customers"
    
    table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']/tbody/tr/td"
    
    
    def __init__(self, driver): 
        self.driver = driver
        
    
    def enter_customer_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)
        
    
    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.textbox_first_name_id).clear() 
        self.driver.find_element(By.ID, self.textbox_first_name_id).send_keys(first_name)
        
        
    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.textbox_last_name_id).clear() 
        self.driver.find_element(By.ID, self.textbox_last_name_id).send_keys(last_name)
        
    
    def enter_company(self, company):
        self.driver.find_element(By.ID, self.textbox_company_id).clear() 
        self.driver.find_element(By.ID, self.textbox_company_id).send_keys(company)
        
    
    def click_search_button(self):
        self.driver.find_element(By.ID, self.button_search_id).click()
        
    
    def get_table_rows_count(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))
    
         
    def search_customer_by_email(self, email):
        email_found = False
        for row in range(1, self.get_table_rows_count() + 1):
            email_field = self.driver.find_element(By.XPATH,
                                                   f"//table[@id='customers-grid']//tbody/tr[{row}]/td[2]").text 
            if email_field == email:
                email_found = True
                break
        
        return email_found
         
         
    def search_customer_by_first_name(self, first_name):
        first_name_found = False
        for row in range(1, self.get_table_rows_count() + 1):
            first_name_field = self.driver.find_element(By.XPATH,
                                                   f"//table[@id='customers-grid']//tbody/tr[{row}]/td[3]").text 
            if first_name in first_name_field:
                first_name_found = True
                break
        
        return first_name_found
         
         
    def search_customer_by_last_name(self, last_name):
        last_name_found = False
        for row in range(1, self.get_table_rows_count() + 1):
            last_name_field = self.driver.find_element(By.XPATH,
                                                   f"//table[@id='customers-grid']//tbody/tr[{row}]/td[3]").text
            if last_name in last_name_field:
                last_name_found = True
                break
        
        return last_name_found
    

    def search_customer_by_company(self, company):
        company_found = False
        for row in range(1, self.get_table_rows_count() + 1):
            company_field = self.driver.find_element(By.XPATH,
                                                   f"//table[@id='customers-grid']//tbody/tr[{row}]/td[5]").text
            if company_field == company:
                company_found = True
                break
        
        return company_found

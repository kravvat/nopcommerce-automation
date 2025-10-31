import time
from base_pages.admin_login_page import AdminLoginPage 
from utilities.read_properties import ReadConfig
from utilities.logger import LogMaker
from utilities import excel_utils

class TestAdminLogin02:
    admin_page_url = ReadConfig.get_admin_page_url()
    logger = LogMaker.generate_log()
    file = ".\\test_data\\admin_login_data.xlsx"
    sheetname = "credentials"
    status_list = []


    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("Starting: TestAdminLogin02 > test_valid_admin_login_data_driven")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_login_page = AdminLoginPage(self.driver)

        self.rows = excel_utils.get_row_count(self.file, self.sheetname)
        for row in range (2, self.rows + 1):
            self.admin_username = excel_utils.read_data(self.file, self.sheetname, row, 1)
            self.admin_password = excel_utils.read_data(self.file, self.sheetname, row, 2)
            self.expect_login = excel_utils.read_data(self.file, self.sheetname, row, 3)

            self.admin_login_page.enter_username(self.admin_username)
            self.admin_login_page.enter_password(self.admin_password)
            self.admin_login_page.click_login()
            time.sleep(1)

            actual_page_title = self.driver.title
            expected_page_title = "Dashboard / nopCommerce administration"
            if expected_page_title == actual_page_title:
                if self.expect_login == "Yes":
                    self.status_list.append("Pass")
                    self.admin_login_page.click_logout()
                elif self.expect_login == "No":
                    self.status_list.append("Fail") 
                    self.logger.warning(f"Defect detected in row {row}")
                    self.admin_login_page.click_logout()
            if expected_page_title != actual_page_title:
                if self.expect_login == "No":
                    self.status_list.append("Pass")
                elif self.expect_login == "Yes":
                    self.status_list.append("Fail")
                    self.logger.warning(f"Defect detected in row {row}")

        if "Fail" in self.status_list:
            self.logger.warning("Test case failed")
            self.driver.close()
            assert False
        else:
            self.logger.info("Test case passed")
            self.driver.close()
            assert True

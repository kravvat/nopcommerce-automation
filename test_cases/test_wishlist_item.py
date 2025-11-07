import time, random, pytest
from utilities.read_properties import ReadConfig
from base_pages.landing_page import LandingPage
from utilities.logger import LogMaker
from utilities.generate_data import GenerateRandomData

class TestWishlistItem05:
    landing_page_url = ReadConfig.get_landing_page_url()
    logger = LogMaker.generate_log()
    
    
    @pytest.mark.beta
    def test_wishlist_item(self, setup):
        self.logger.info(f"Starting: TestWishlistItem05 > test_wishlist_item")
        self.driver = setup 
        self.category = GenerateRandomData.generate_random_category()

        self.driver.maximize_window()
        self.driver.get(self.landing_page_url)
        self.landing_page = LandingPage(self.driver, self.category)
        self.landing_page.click_category()

        time.sleep(5)
        self.driver.close()

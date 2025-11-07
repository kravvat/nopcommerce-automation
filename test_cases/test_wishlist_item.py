import time, pytest
from utilities.read_properties import ReadConfig
from base_pages.landing_page import LandingPage
from base_pages.subcategory_page import SubcategoryPage
from utilities.logger import LogMaker
from utilities.generate_data import GenerateRandomData

class TestWishlistItem05:
    landing_page_url = ReadConfig.get_landing_page_url()
    logger = LogMaker.generate_log()
    
    
    @pytest.mark.beta
    @pytest.mark.parametrize("instance_id", range(10))
    def test_wishlist_item(self, setup, instance_id):
        self.logger.info(f"Starting: TestWishlistItem05 > test_wishlist_item | Instance #{instance_id}")
        self.driver = setup 
        self.category = GenerateRandomData.generate_random_category()
        self.has_subcategory = self.category in [
            "computers",
            "electronics",
            "apparel",
        ]

        self.driver.maximize_window()
        self.driver.get(self.landing_page_url)
        self.landing_page = LandingPage(self.driver, self.category)
        self.logger.info(f"self.category --> {self.category} | Instance #{instance_id}")
        self.landing_page.click_category()

        if self.has_subcategory:
            self.subcategory = GenerateRandomData.generate_random_subcategory(self.category)
            self.subcategory_page = SubcategoryPage(self.driver, self.subcategory)
            self.logger.info(f"self.subcategory --> {self.subcategory} | Instance #{instance_id}")
            self.subcategory_page.click_subcategory()

        # time.sleep(3)
        self.driver.close()
import pytest
from utilities.read_properties import ReadConfig
from base_pages.landing_page import LandingPage
from base_pages.subcategory_page import SubcategoryPage
from base_pages.products_page import ProductsPage
from base_pages.product_page import ProductPage
from base_pages.wishlist_page import WishlistPage
from utilities.logger import LogMaker
from utilities.generate_data import GenerateRandomData


class TestWishlistItem05:
    landing_page_url = ReadConfig.get_landing_page_url()
    logger = LogMaker.generate_log()
    
    
    @pytest.mark.parametrize("instance_id", range(10))
    def test_add_product_to_wishlist(self, setup, instance_id):
        self.logger.info(f"Starting: TestWishlistItem05 > test_add_product_to_wishlist | Instance #{instance_id}")
        self.driver = setup 
        # self.category = GenerateRandomData.generate_random_category()
        self.product_name = "pride-and-prejudice" 
        self.category = "books"
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

        self.products_page = ProductsPage(self.driver, self.product_name) # Hardcoded for simplicity
        self.products_page.click_product_name()

        self.products_page = ProductPage(self.driver)
        self.products_page.click_add_to_wishlist()
        self.products_page.click_wishlist() 
        
        self.wishlist_page = WishlistPage(self.driver, self.product_name)
        if self.wishlist_page.search_product():
            assert True
            self.logger.info(f"Success: Product added to the wishlist | Instance #{instance_id}")
            self.driver.close()
        else:
            self.logger.warning(f"Fail: Product has not been added to the wishlist | Instance #{instance_id}")    
            self.driver.save_screenshot(f".\\screenshots\\test_add_product_to_wishlist.png")
            self.driver.close()
            assert False
        
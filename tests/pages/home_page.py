from tests.pages.base_page import BasePage
from tests.utils.config import CONFIG

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_box = "input#small-searchterms"
        self.search_button = "button[type='submit'][class*='search-box-button']"
        self.product_titles = "h2.product-title a"
        self.no_results_message = "div.no-result"
        self.base_url = CONFIG["env"]["base_url"]

    def open(self):
        self.open_url(f"{self.base_url}/")\
        
    def navigate_to_category(self, category_name):
        category_selector = f"a[href*='{category_name.lower()}']"
        self.click(category_selector)

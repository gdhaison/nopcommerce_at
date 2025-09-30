from tests.pages.base_page import BasePage
from tests.utils.config import CONFIG

class SearchProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_box = "input#small-searchterms"
        self.search_button = "button[type='submit'][class*='search-box-button']"
        self.product_titles = "h2.product-title a"
        self.no_results_message = "div.no-result"
        self.base_url = CONFIG["env"]["base_url"]

    def open(self):
        self.open_url(f"{self.base_url}/")

    def search_product(self, product_name):
        self.fill(self.search_box, product_name)
        self.click(self.search_button)

    def get_product_titles(self):
        return [element.inner_text() for element in self.page.locator(self.product_titles).all()]

    def is_no_results_message_displayed(self):
        return self.is_visible(self.no_results_message)

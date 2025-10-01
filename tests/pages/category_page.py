from tests.pages.base_page import BasePage
from tests.utils.config import CONFIG
import time
from tests.utils.logger import logger
import re

class CategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_titles = "h2.product-title a"
        self.sort_selector = "select#products-orderby"
        self.manufacturer_checkbox = "//label[contains(., '{}')]/preceding-sibling::input"
        self.base_url = CONFIG["env"]["base_url"]

    def open(self, category_slug):
        self.open_url(f"{self.base_url}/{category_slug}")

    def get_product_titles(self):
        return [element.inner_text() for element in self.page.locator(self.product_titles).all()]
    
    def sort_products(self, sort_option):
        self.wait_for_selector(self.sort_selector)
        time.sleep(1)
        self.page.select_option(self.sort_selector, label=sort_option)
        self.page.eval_on_selector(self.sort_selector, "el => el.dispatchEvent(new Event('change'))")
        time.sleep(1)
        # self.wait_for_selector(self.product_titles)

        # self.page.wait_for_load_state("load")
        # self.page.wait_for_load_state("networkidle")
        

    # def sort_products(self, sort_option_label):
    #     # Mở dropdown
    #     self.page.click(self.sort_selector)
    #     # Click option cần chọn
    #     self.page.click("//option[text()='Price: Low to High']")
    #     # Chờ sản phẩm load lại
    #     self.page.wait_for_selector("h2.product-title")

    def get_product_prices(self):
        price_selector = "span.price"
        prices = []
        for element in self.page.locator(price_selector).all():
            price_text = element.inner_text().replace("$", "").replace(",", "").strip()
            try:
                prices.append(float(price_text))
            except ValueError:
                continue
        return prices
    
    def filter_by_manufacturer(self, manufacturer_name):
        self.wait_for_selector(self.manufacturer_checkbox.format(manufacturer_name))
        manufacturer_checkbox = self.manufacturer_checkbox.format(manufacturer_name)
        self.click(manufacturer_checkbox)
        self.wait_for_selector(self.product_titles)
        self.page.wait_for_load_state("networkidle")


    def drag_price_slider(self, min_price, max_price):
        min_price = int(min_price)
        max_price = int(max_price)

        slider = self.page.locator("#price-range-slider").bounding_box()
        slider_min, slider_max = 0, 10000
        slider_width = slider["width"]

        min_offset = (min_price - slider_min) / (slider_max - slider_min) * slider_width + 1.5
        max_offset = (max_price - slider_min) / (slider_max - slider_min) * slider_width + 1.5

        target_min_x = slider["x"] + min_offset
        target_max_x = slider["x"] + max_offset
        target_y = slider["y"] + slider["height"] / 2

        # handle min
        min_handle = self.page.locator("#price-range-slider span").nth(0)
        min_box = min_handle.bounding_box()
        start_min_x = min_box["x"] + min_box["width"] / 2
        start_min_y = min_box["y"] + min_box["height"] / 2

        self.page.mouse.move(start_min_x, start_min_y)
        self.page.mouse.down()
        self.page.mouse.move(target_min_x, target_y, steps=30)
        self.page.mouse.up()

        # handle max
        max_handle = self.page.locator("#price-range-slider span").nth(1)
        max_box = max_handle.bounding_box()
        start_max_x = max_box["x"] + max_box["width"] / 2
        start_max_y = max_box["y"] + max_box["height"] / 2

        self.page.mouse.move(start_max_x, start_max_y)
        self.page.mouse.down()
        self.page.mouse.move(target_max_x, target_y, steps=10)
        self.page.mouse.up()

        # lấy text hiển thị
        selected_text = self.page.locator(".selected-price-range").inner_text().strip()
        logger.info(f"Raw slider text: {repr(selected_text)}")

        # chuẩn hoá: lấy toàn bộ số trong chuỗi
        numbers = re.findall(r"\d+", selected_text)
        if len(numbers) >= 2:
            min_val, max_val = map(int, numbers[:2])
        else:
            raise ValueError(f"Không parse được giá trị từ slider text: {selected_text}")

        logger.info(f"Parsed values: min={min_val}, max={max_val}")

        # verify (±100 để tránh rounding UI)
        assert abs(min_val - min_price) <= 100, f"Expected around {min_price}, but got {min_val}"
        assert abs(max_val - max_price) <= 100, f"Expected around {max_price}, but got {max_val}"

    def get_product_prices(self):
        price_selector = "span.price"
        prices = []
        for element in self.page.locator(price_selector).all():
            price_text = element.inner_text().replace("$", "").replace(",", "").strip()
            try:
                prices.append(float(price_text))
            except ValueError:
                continue
        return prices
    
    def is_no_products_message_displayed(self):
        no_products_selector = "div.no-result"
        return self.is_visible(no_products_selector)

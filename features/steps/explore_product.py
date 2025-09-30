from behave import given, when, then
from tests.pages.home_page import HomePage
from tests.pages.category_page import CategoryPage
from tests.utils.logger import logger

@when('I navigate to "{}" category')
def step_navigate_to_category(context, category_name):
    context.home_page.navigate_to_category(category_name)
    context.category_page = CategoryPage(context.page)

@when('I sort products by "{sort_option}"')
def step_sort_products(context, sort_option):
    context.category_page.sort_products(sort_option)

@when('I filter products by manufacturer "{manufacturer}"')
def step_filter_by_manufacturer(context, manufacturer):
    context.category_page.filter_by_manufacturer(manufacturer)
    context.category_page.page.wait_for_load_state("networkidle")

@when('I set the price filter from "{min_price}" to "{max_price}"')
def step_set_price_filter(context, min_price, max_price):
    context.category_page.drag_price_slider(min_price, max_price)
    context.category_page.page.wait_for_load_state("networkidle")

@then('I should see a list of products under "{category_name}"')
def step_verify_products_in_category(context, category_name):
    product_titles = context.category_page.get_product_titles()
    assert product_titles, f"No products found under category '{category_name}'"

@then('the products should be displayed in ascending order of price')
def step_verify_products_sorted_by_price(context):
    product_prices = context.category_page.get_product_prices()
    sorted_prices = sorted(product_prices)
    assert product_prices == sorted_prices, "Products are not sorted by price in ascending order"

@then('the products should be displayed in descending order of price')
def step_verify_products_sorted_by_price_desc(context):
    product_prices = context.category_page.get_product_prices()
    sorted_prices = sorted(product_prices, reverse=True)
    logger.info(f"Product prices: {product_prices}")
    logger.info(f"Sorted prices: {sorted_prices}")

    assert product_prices == sorted_prices, "Products are not sorted by price in descending order"

@then('only "{manufacturer}" products should be shown')
def step_verify_products_filtered_by_manufacturer(context, manufacturer):
    context.category_page.page.wait_for_load_state("networkidle")
    product_titles = context.category_page.get_product_titles()
    assert product_titles, "No products found after applying manufacturer filter"
    assert all(manufacturer.lower() in title.lower() for title in product_titles), \
        f"Not all products are from manufacturer '{manufacturer}'"
    
@then('only products with price between "{min_price}" and "{max_price}" should be shown')
def step_verify_products_filtered_by_price_range(context, min_price, max_price):
    min_price = float(min_price)
    max_price = float(max_price)
    product_prices = context.category_page.get_product_prices()
    assert product_prices, "No products found after applying price filter"
    assert all(min_price <= price <= max_price for price in product_prices), \
        f"Some products are outside the price range {min_price} - {max_price}"
    
@then('I should see no products available message')
def step_verify_no_products_message(context):
    context.category_page.page.wait_for_load_state("networkidle")
    assert context.category_page.is_no_products_message_displayed(), \
        "Expected no products message to be displayed, but it was not."

    
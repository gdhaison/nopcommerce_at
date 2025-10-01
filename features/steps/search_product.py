from behave import given, when, then
from tests.pages.search_product_page import SearchProductPage
from playwright.sync_api import Dialog
from playwright.sync_api import sync_playwright

import time

@given("I am on the search products page")
def step_open_registration_page(context):
    context.search_product_page = SearchProductPage(context.page)
    context.search_product_page.open()

@when('I search for product "{product_name}"')
def step_search_product(context, product_name):
    context.search_product_page.search_product(product_name)

@when('I search for product with empty value then verify alert')
def step_search_product_empty(context):
    dialog_triggered = {"called": False}

    def handle_dialog(dialog: Dialog):
        dialog_triggered["called"] = True
        assert dialog.message == "Please enter some search keyword", \
            f"Expected alert message 'Please enter some search keyword', but got '{dialog.message}'"
        dialog.accept()

    context.page.on("dialog", handle_dialog)

    try:
        context.search_product_page.search_product("")
    except TimeoutError:
        if not dialog_triggered["called"]:
            raise AssertionError("Expected alert dialog did not appear")
        

@then('I should see products related to "{product_name}"')
def step_verify_product_in_results(context, product_name):
    titles = context.search_product_page.get_product_titles()
    assert all(product_name.lower() in title.lower() for title in titles), \
        f"Expected to find '{product_name}' in search results, but got: {titles}"

@then('I should see "{product_name}" in the search results')
def step_verify_product_in_results(context, product_name):
    titles = context.search_product_page.get_product_titles()
    assert any(product_name.lower() in title.lower() for title in titles), \
        f"Expected to find '{product_name}' in search results, but got: {titles}"
    
@then('I should see no result message')
def step_verify_no_results_message(context):
    assert context.search_product_page.is_no_results_message_displayed(), \
        "Expected no results message to be displayed, but it was not."
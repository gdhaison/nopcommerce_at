from behave import given, when, then
from playwright.sync_api import sync_playwright
import os
import time
from tests.pages.register_page import RegisterPage

@given("I am on the registration page")
def step_open_registration_page(context):
    context.register_page.open()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    path = os.path.join("reports", filename)

    # Lưu ảnh vào thư mục reports
    context.page.screenshot(path=path, full_page=True)


@when("I register with a random yopmail")
def step_register_random_yopmail(context):
    context.registered_email = context.register_page.register_random_yopmail()

@then("I should see the registration success message")
def step_verify_registration(context):
    assert context.register_page.is_registration_successful()
    #sleep 100 to check email in yopmail
from behave import given, when, then
from tests.pages.home_page import HomePage

@given("I am on the homepage")
def step_open_homepage(context):
    context.home_page = HomePage(context.page)
    context.home_page.open()

@when("I click \"{text}\"")
def step_click(context, text):
    context.home_page.click('a:has-text(' + f'"{text}"' + ')')

@when('I Sleep for "{seconds}" seconds')
def step_sleep(context, seconds):
    import time
    time.sleep(int(seconds))

@when("I open a new tab")
def step_open_new_tab(context):
    context.new_page = context.page.context.new_page()
    context.page = context.new_page 

@when('I go to website "{url}"')
def step_go_to_website(context, url):
    context.page.goto(url)

@when('I input email "{email}"')
def step_input_email(context, email):
    context.page.fill('input.ycptinput', email)

@when('I click button search mail')
def step_click_search_mail(context):
    context.page.click("button[title='Check Inbox @yopmail.com']")

@then('email from nopcommerce should be visible')
def step_verify_email_visible(context):
    assert context.page.is_visible("text=nopCommerce"), "Email from nopcommerce is not visible"



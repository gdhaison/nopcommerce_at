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


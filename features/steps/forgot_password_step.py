from behave import given, when, then
from tests.pages.forgot_password_page import ForgotPasswordPage
from tests.utils.logger import logger

@given("I am on the forgot password page")
def step_open_forgot_password_page(context):
    context.forgot_password_page = ForgotPasswordPage(context.page)
    context.forgot_password_page.open()

@when('I enter an email address "{email}"')
def step_enter_valid_email(context, email):
    assert context.forgot_password_page.is_valid_email_format(email), f"Email format is invalid: {email}"
    context.forgot_password_page.submit_email(email)

@when('I click on RECOVER')
def step_click_button(context):
    context.forgot_password_page.click(f'button:has-text("RECOVER")')

@then('I should see an email error message "{expected_message}"')
def step_verify_error_message(context, expected_message):
    actual_message = context.forgot_password_page.get_email_field_error()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"
    logger.info(f"Error message verified: {actual_message}")

@then('I should see a message "{expected_message}"')
def step_verify_confirmation_message(context, expected_message):
    actual_message = context.forgot_password_page.get_success_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"
    logger.info(f"Confirmation message verified: {actual_message}")

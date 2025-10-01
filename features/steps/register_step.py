from behave import given, when, then
from tests.pages.register_page import RegisterPage
import time

@given("I am on the registration page")
def step_open_registration_page(context):
    context.register_page = RegisterPage(context.page)
    context.register_page.open()

@when("I register with a random yopmail")
def step_register_random_yopmail(context):
    context.registered_email = context.register_page.register_random_yopmail()

@when("I register with a special yopmail")
def step_register_random_yopmail(context):
    context.registered_email = context.register_page.register_random_yopmail()


@then("I should see the registration success message")
def step_verify_registration(context):
    assert context.register_page.is_registration_successful(), \
        "Expected success message, but registration failed!"

@when('I register with an existing email "{email}"')
def step_register_existing_email(context, email):
    context.register_page.register_with_email(email=email)

@when('I register with email "{email}"')
def step_register_email(context, email):
    context.register_page.register_with_email(email=email)

@when('I register detail with email "{email}" and first name "{first}" and last name "{last}" and password "{password}" and confirm password "{confirm_password}"') 
def step_register_detailed(context, email, first, last, password, confirm_password):
    context.register_page.register_with_email(
        email=email,
        first=first,
        last=last,
        password=password,
        confirm_password=confirm_password
    )

@when('I click register without filling any fields')
def step_register_email_without_filling(context):
    context.register_page.click_register()
    context.page.wait_for_timeout(1000)

@then('I should see an error message "{message}"')
def step_verify_error_message(context, message):
    actual = context.register_page.get_error_message()
    assert message in actual, f"Expected '{message}', got '{actual}'"

@then('I should see an error message from email field "{message}"')
def step_verify_error_message_email(context, message):
    actual = context.register_page.get_email_error()
    assert message in actual, f"Expected '{message}', got '{actual}'"

@then('I should see an error message from password field "{message}"')
def step_verify_error_message_email(context, message):
    actuals = context.register_page.get_field_errors()
    assert len(actuals) == 1, "Expected one error message but got none"
    assert message in actuals, f"Expected '{message}', got '{actuals[0]}'"

@when("I submit the registration form without filling any fields")
def step_register_empty(context):
    context.register_page.click(context.register_page.register_button)

@then("I should see required field validation errors")
def step_verify_required_fields(context):
    errors = context.register_page.get_field_errors()
    assert len(errors) == 5, "Expected validation errors but got none"


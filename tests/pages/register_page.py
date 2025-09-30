import random
import string
from tests.pages.base_page import BasePage
from tests.utils.config import CONFIG
from tests.utils.logger import logger

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.gender_male = "input#gender-male"
        self.first_name = "input#FirstName"
        self.last_name = "input#LastName"
        self.email = "input#Email"
        self.password = "input#Password"
        self.confirm_password = "input#ConfirmPassword"
        self.password_error = "span#Password-error"
        self.register_button = "button#register-button"
        self.success_message = "div.result"
        self.error_message = "div.message-error"
        self.email_error = "span#Email-error"
        self.field_error = ".field-validation-error"
        self.base_url = CONFIG["env"]["base_url"]

    def open(self):
        self.open_url(f"{self.base_url}/register")

    def generate_random_email(self):
        random_str = ''.join(random.choices(string.ascii_lowercase, k=8))
        return f"{random_str}@yopmail.com"

    def register_random_yopmail(self, first="John", last="Doe", password="Password123!"):
        email = self.generate_random_email()
        self.click(self.gender_male)
        self.fill(self.first_name, first)
        self.fill(self.last_name, last)
        self.fill(self.email, email)
        self.fill(self.password, password)
        self.fill(self.confirm_password, password)
        self.click(self.register_button)
        return email

    def register_with_email(self, email, first="John", last="Doe", password="Password123!", confirm_password=None):
        if not confirm_password:
            confirm_password = password
        self.click(self.gender_male)
        self.fill(self.first_name, first)
        self.fill(self.last_name, last)
        self.fill(self.email, email)
        self.fill(self.password, password)
        self.fill(self.confirm_password, confirm_password)
        self.click(self.register_button)
    
    def click_register(self):
        self.click(self.register_button)

    def is_registration_successful(self):
        return "Your registration completed" in self.get_text(self.success_message)

    def get_error_message(self):
        return self.get_text(self.error_message)
    
    def get_email_error(self):
        return self.get_text(self.email_error)
    
    def get_password_error(self):
        return self.get_text(self.password_error)

    def get_field_errors(self):
        elements = self.page.locator(self.field_error).all()
        errors = [el.inner_text().strip() for el in elements if el.inner_text().strip()]

        return errors

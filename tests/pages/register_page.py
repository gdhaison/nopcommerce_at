import random
import string
from tests.pages.base_page import BasePage
from tests.utils.config import CONFIG

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.gender_male = "input#gender-male"
        self.first_name = "input#FirstName"
        self.last_name = "input#LastName"
        self.email = "input#Email"
        self.password = "input#Password"
        self.confirm_password = "input#ConfirmPassword"
        self.register_button = "button#register-button"
        self.success_message = "div.result"
        self.base_url = CONFIG["env"]["base_url"]

    def open(self):
        self.open_url(f"{self.base_url}/register")

    def generate_random_email(self):
        random_str = ''.join(random.choices(string.ascii_lowercase, k=8))
        return f"{random_str}@yopmail.com"

    # def register(self, first="John", last="Doe", password="Password123!"):
    #     email = self.generate_random_email()
    #     self.click(self.gender_male)
    #     self.fill(self.first_name, first)
    #     self.fill(self.last_name, last)
    #     self.fill(self.email, email)
    #     self.fill(self.password, password)
    #     self.fill(self.confirm_password, password)
    #     self.click(self.register_button)
    #     return email
    
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

    def is_registration_successful(self):
        return "Your registration completed" in self.get_text(self.success_message)

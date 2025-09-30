from tests.pages.base_page import BasePage
from tests.utils.config import CONFIG
import time
from tests.utils.logger import logger
import re

class ForgotPasswordPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "input#Email"
        self.submit_button = "button[type='submit'][class*='button-1']"
        self.success_message = "p.content"
        self.error_message = "div.message-error"
        self.field_error = "span.field-validation-error"
        self.base_url = CONFIG["env"]["base_url"]

    def open(self):
        self.open_url(f"{self.base_url}/passwordrecovery")

    def submit_email(self, email):
        self.fill(self.email_input, email)

    def get_success_message(self):
        self.wait_for_selector(self.success_message)
        return self.get_text(self.success_message)
    
    def get_email_field_error(self):
        self.wait_for_selector(self.field_error)
        return self.get_text(self.field_error)

    def get_error_message(self):
        self.wait_for_selector(self.error_message)
        return self.get_text(self.error_message)

    def is_valid_email_format(self, email):
        # Simple regex for email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    def is_success_message_displayed(self, expected_message):
        actual_message = self.get_success_message()
        return expected_message in actual_message
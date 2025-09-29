from playwright.sync_api import sync_playwright
from tests.pages.register_page import RegisterPage
import os
import time
from behave.model_core import Status



def before_all(context):
    context.playwright = sync_playwright().start()
    docker_env = os.getenv("DOCKER_ENV", "false").lower() == "true"

    if docker_env:
        context.browser = context.playwright.chromium.launch(headless=True)
    else:
        context.browser = context.playwright.chromium.launch(headless=False, channel="chrome")

    context.browser_context = context.browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800}
    )
    context.page = context.browser_context.new_page()

    context.register_page = RegisterPage(context.page)

def after_step(context, step):
    if step.status == Status.failed:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshot_{step.name}_{timestamp}.png"
        path = os.path.join("reports", filename)

        context.page.screenshot(path=path, full_page=True)

def after_all(context):
    context.browser.close()
    context.playwright.stop()
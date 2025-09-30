from playwright.sync_api import sync_playwright
from tests.pages.register_page import RegisterPage
import os
import time
from behave.model_core import Status
from tests.utils.logger import logger   # 👈 import logger

def before_all(context):
    logger.info("=== Test suite starting ===")
    context.playwright = sync_playwright().start()

    is_ci = os.getenv("CI") or os.getenv("DOCKER_ENV")
    if is_ci:
        logger.info("Running in CI/Docker mode: launching Chromium headless")
        context.browser = context.playwright.chromium.launch(headless=True)
    else:
        logger.info("Running in local mode: launching Chrome with UI")
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

    logger.info("Browser and context initialized successfully")

def before_scenario(context, scenario):
    logger.info(f"===== START SCENARIO: {scenario.name} =====")

def after_step(context, step):
    if step.status == Status.failed:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshot_{step.name}_{timestamp}.png"
        path = os.path.join("reports", filename)
        context.page.screenshot(path=path, full_page=True)
        logger.error(f"Step FAILED: {step.name} → Screenshot saved at {path}")
    else:
        logger.info(f"Step PASSED: {step.name}")

def after_all(context):
    logger.info("Closing browser and stopping Playwright")
    context.browser.close()
    context.playwright.stop()
    logger.info("=== Test suite finished ===")

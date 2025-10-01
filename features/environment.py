from playwright.sync_api import sync_playwright
from tests.pages.register_page import RegisterPage
import os
import time
from behave.model_core import Status
from tests.utils.logger import logger

def before_all(context):
    logger.info("=== Test suite starting ===")
    context.playwright = sync_playwright().start()

    browser_name = context.config.userdata.get("browser", "chromium")
    if browser_name == "firefox":
        is_ci = os.getenv("CI") or os.getenv("DOCKER_ENV")
        if is_ci:
            logger.info("Running in CI/Docker mode: launching firefox headless")
            context.browser = context.playwright.firefox.launch(headless=True)
        else:
            logger.info("Running in local mode: launching Webkit with UI")
            context.browser = context.playwright.firefox.launch(headless=False)
    
    elif browser_name == "chromium":

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

    # if step.status == "failed":
    #     # tạo folder lưu screenshot
    #     os.makedirs("reports/screenshots", exist_ok=True)
    #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     filename = f"reports/screenshots/{step.name}_{timestamp}.png"

    #     # chụp màn hình
    #     context.page.screenshot(path=filename, full_page=True)

    #     # attach vào behave report (nếu formatter hỗ trợ, ví dụ behave-html-formatter)
    #     if hasattr(context, "embed"):
    #         with open(filename, "rb") as image_file:
    #             context.embed("image/png", image_file.read(), filename)

    if step.status == Status.failed:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshot_{step.name}_{timestamp}.png"
        filepath = os.path.join("reports", filename)
        context.page.screenshot(path=filepath, full_page=True)
        logger.error(f"Step FAILED: {step.name}. Screenshot saved to {filepath}")
        # Attach screenshot to the step for reporting (if supported by formatter)

        if not hasattr(step, "attachments"):
            step.attachments = []
        step.attachments.append(filepath)
    else:
        logger.info(f"Step PASSED: {step.name}")

def after_all(context):
    logger.info("Closing browser and stopping Playwright")
    context.browser.close()
    context.playwright.stop()
    logger.info("=== Test suite finished ===")

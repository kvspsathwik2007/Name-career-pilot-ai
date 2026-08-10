from playwright.async_api import async_playwright
import os


class BrowserManager:
    def __init__(self):
        self.user_data_dir = os.path.join(
            os.environ["USERPROFILE"],
            "AppData",
            "Local",
            "Microsoft",
            "Edge",
            "User Data"
        )

    async def launch(self):
        playwright = await async_playwright().start()

        browser = await playwright.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,
            channel="msedge",
            headless=False
        )

        page = browser.pages[0] if browser.pages else await browser.new_page()

        return playwright, browser, page
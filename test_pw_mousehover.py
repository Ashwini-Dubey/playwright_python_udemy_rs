import time
from playwright.sync_api import Page, expect


def test_pw_web_tables_handler(page: Page):
    # Navigate to the website
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()
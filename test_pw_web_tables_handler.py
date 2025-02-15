import time
from playwright.sync_api import Page, expect


def test_pw_web_tables_handler(page: Page):
    # Navigate to the website
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColValue = index
            print(priceColValue)
            break

    riceRow = page.locator("tr").filter(has_text="Potato")

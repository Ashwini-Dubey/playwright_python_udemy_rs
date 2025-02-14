import time
from playwright.sync_api import Page, expect


def test_pw_e2e_first(page: Page):
    # Navigate to the website
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    # List of products to add to the cart
    products = ["Brocolli", "Cauliflower", "Cucumber", "Beetroot", "Carrot"]

    # Loop through each product and add it to the cart
    for product in products:
        page.locator(".product").filter(has_text=product).get_by_role("button").click()

    # Click on the cart icon
    page.locator("//img[@alt='Cart']").click()

    # Proceed to checkout
    page.get_by_role("button", name="PROCEED TO CHECKOUT").click()

    # Click on "Place Order" button
    page.get_by_role("button", name="Place Order").click()

    # Select country from the dropdown
    page.locator("select").select_option("India")

    # Agree to terms and conditions by clicking the checkbox
    page.get_by_role("checkbox").click()

    # Click on the final "Proceed" button to complete the order
    page.get_by_role("button", name="Proceed").click()

    # Verify that the success message "Thank you" is visible
    expect(page.get_by_text("Thank you")).to_be_visible()

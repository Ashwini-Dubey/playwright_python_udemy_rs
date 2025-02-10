from playwright.sync_api import Page, expect

def test_pw_invalid_login(page: Page):
    """
    Test invalid login functionality using Playwright locators
    and dynamic selection of products.
    """

    # Navigate to the login page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # Fill in the Username field using get_by_label
    page.get_by_label("Username:").fill("rahulshettyacademy")

    # Fill in the Password field using get_by_label
    page.get_by_label("Password:").fill("learning")

    # Select "Consultant" from the Student/Teacher/Consultant dropdown
    page.get_by_role("combobox").select_option("consult")

    # Check the "Terms and Conditions" checkbox using its ID selector
    page.locator("#terms").check()

    # Click the "Sign In" button to submit the form
    page.get_by_role("button", name="Sign In").click()

    # Dynamically locate and add "iPhone X" to the cart
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()  # Click the "Add to Cart" button

    # Dynamically locate and add "Nokia Edge" to the cart
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()  # Click the "Add to Cart" button

    # Click on the "Checkout" button
    page.get_by_text("Checkout").click()

    # Assert that exactly two products are in the cart
    expect(page.locator(".media-body")).to_have_count(2)

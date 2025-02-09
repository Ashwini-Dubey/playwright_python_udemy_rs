from playwright.sync_api import Page, expect, Playwright

def test_pw_invalid_login_nightly(playwright: Playwright):
    """ Test invalid login functionality using Playwright locators """

    # Initialize the Playwright instance and launch the Firefox browser in non-headless mode
    # Note: Playwright uses a patched version of Firefox Nightly by default.
    # To use the stable Firefox version, use `channel="firefox"` when launching.
    page = playwright.firefox.launch(headless=False).new_page()

    # Navigate to the login page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    print(page.evaluate("navigator.userAgent"))

    # Fill in the Username field using get_by_label
    page.get_by_label("Username:").fill("rahulshettyacademy")

    # Fill in the Password field using get_by_label
    page.get_by_label("Password:").fill("learning123")

    # Select an option from the Student/Teacher/Consultant dropdown using get_by_role("combobox")
    page.get_by_role("combobox").select_option("consult")

    # Check the "Terms and Conditions" checkbox using its ID
    page.locator("#terms").check()

    # Click on the "Terms and Conditions" link
    page.get_by_role("link", name="terms and conditions").click()

    # Click on the "Sign In" button to submit the form
    page.get_by_role("button", name="Sign In").click()

    # Validate that the error message appears for incorrect login credentials
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    # Close the browser instance to free up resources
    page.close()

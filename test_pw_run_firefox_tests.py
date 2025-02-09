from playwright.sync_api import Page, expect, Playwright

def test_pw_invalid_login_firefox(playwright: Playwright):
    """
    Test invalid login functionality using Playwright locators in Firefox.

    This test launches Firefox in non-headless mode, attempts to log in with incorrect
    credentials, and verifies that the appropriate error message is displayed.
    """

    # Initialize the Playwright instance and launch the **stable** Firefox browser
    # `channel="firefox"` ensures the test runs on the user's installed Firefox version
    # instead of Playwright's default Nightly build.
    page = playwright.firefox.launch(channel="firefox", headless=False).new_page()

    # Navigate to the login page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    print(page.evaluate("navigator.userAgent"))

    # Fill in the Username field using get_by_label
    page.get_by_label("Username:").fill("rahulshettyacademy")

    # Fill in the Password field using get_by_label
    page.get_by_label("Password:").fill("learning123")  # Incorrect password for test validation

    # Select an option from the Student/Teacher/Consultant dropdown using get_by_role("combobox")
    page.get_by_role("combobox").select_option("consult")

    # Check the "Terms and Conditions" checkbox using its ID selector
    page.locator("#terms").check()

    # Click on the "Terms and Conditions" link (for additional interaction)
    page.get_by_role("link", name="terms and conditions").click()

    # Click on the "Sign In" button to submit the form
    page.get_by_role("button", name="Sign In").click()

    # Validate that the error message appears for incorrect login credentials
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    # Close the browser instance to free up system resources
    page.close()

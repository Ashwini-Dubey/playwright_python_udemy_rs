from playwright.sync_api import Page, expect

def test_pw_expect(page: Page):
    """ Test invalid login functionality using Playwright locators """

    # Navigate to the login page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

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

    # Validate that error message appears
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
from playwright.sync_api import Page, expect

def test_pw_visible_invisible_assertions(page: Page):
    """
    Test visibility toggle functionality using Playwright.
    """

    # Navigate to the Automation Practice page
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Verify that the input field with placeholder "Hide/Show Example" is initially visible
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    # Click the "Hide" button to hide the input field
    page.get_by_role("button", name="Hide").click()

    # Verify that the input field is now hidden
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Click the "Show" button to make the input field visible again
    page.get_by_role("button", name="Show").click()

    # Verify that the input field is visible after clicking "Show"
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

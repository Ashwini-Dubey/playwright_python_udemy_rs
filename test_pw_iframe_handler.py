from playwright.sync_api import Page, expect

def test_pw_child_window_tabs_handler(page: Page):
    """
    This test automates interactions with an iframe on the Automation Practice page.
    It navigates to the webpage, locates the iframe, clicks on a link inside the iframe,
    and verifies that the expected text appears.
    """

    # Step 1: Navigate to the Automation Practice webpage
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Step 2: Locate the iframe using its ID selector
    frame_page = page.frame_locator("#courses-iframe")

    # Step 3: Click on the "All Access Plan" link inside the iframe
    frame_page.get_by_role("link", name="All Access Plan").click()

    # Step 4: Verify that the iframe contains the text "Happy Subscribers"
    expect(frame_page.locator("body")).to_contain_text("Happy Subscibers")

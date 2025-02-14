from playwright.sync_api import Page, expect

def test_pw_alerts_popups_handler(page: Page):
    """
    Test handling JavaScript alert and confirm popups using Playwright.
    """

    # Navigate to the Automation Practice page
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Handle confirmation dialog (Clicking "Confirm" button)
    page.on("dialog", lambda dialog: dialog.accept())  # Automatically accept the dialog
    page.get_by_role("button", name="Confirm").click()

    # Handle alert dialog (Clicking "Alert" button)
    page.on("dialog", lambda dialog: dialog.accept())  # Accept the alert
    page.get_by_role("button", name="Alert").click()

    # Handle alert dialog again, but this time dismiss it
    page.on("dialog", lambda dialog: dialog.dismiss())  # Dismiss the alert
    page.get_by_role("button", name="Alert").click()

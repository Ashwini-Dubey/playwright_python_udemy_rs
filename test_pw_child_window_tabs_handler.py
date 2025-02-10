from playwright.sync_api import Page, expect

def test_pw_child_window_tabs_handler(page: Page):
    """
    Test handling of child windows (popups) in Playwright.
    """

    # Navigate to the login page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # Expect a new tab (popup) to open when clicking the blinking text
    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").click()  # Click the link that opens a new window/tab

    # Get the reference to the newly opened child page
    child_page = new_page_info.value

    # Locate the element with class "red" on the child page and extract its text content
    text = child_page.locator(".red").text_content()

    # Print the extracted text from the child window
    print(text)

    # Extract the email from the text using string manipulation
    words = text.split("at")  # Split the text at "at"
    email = words[1].strip().split(" ")[0]  # Take the first word after "at", which is the email

    # Print the extracted email
    print(email)

    # Validate the extracted email using an assertion
    assert email == "mentor@rahulshettyacademy.com"

from playwright.sync_api import Playwright

# Works with the browsers such as firefox , chromium engine in headed mode.
# This can be used when working with the frameworks
def test_pw_browser_launcher(playwright):
    # To run the browser in headed mode
    browser = playwright.firefox.launch(headless=False)

    # To run the browser in headless mode
    # playwright.chromium.launch()

    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    



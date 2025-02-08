# Works only with chromium engine in headless mode
# This will not work in case of custom requirements such as headed mode or running with firefox mode.
def test_pw_shortcut(page):
    page.goto("https://rahulshettyacademy.com")

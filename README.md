# Playwright for Web and API Automation using Python

## 1. Introduction
Playwright is a powerful automation framework that supports web and API testing. It is designed to be fast, reliable, and capable of handling modern web applications with ease. Playwright supports multiple browsers, including Chromium, Firefox, and WebKit, and allows automation in headless or headed mode.

## 2. Installation and Setup

### Install Playwright
To use Playwright with Python, install it using pip:
```sh
pip install playwright
```

### Install Browsers
After installation, install the necessary browser binaries:
```sh
playwright install
```

To install only a specific browser:
```sh
playwright install chromium
```

### Verify Installation
You can check the installation by running:
```sh
python -m playwright --version
```

## 3. Web Automation with Playwright

### Launching a Browser
```python
def test_pw_shortcut(page):
    page.goto("https://rahulshettyacademy.com")
```

### Interacting with Web Elements
```python
page.fill("#username", "test_user")  # Enter text
page.fill("#password", "password123")
page.click("#login")  # Click button
```

### Handling Assertions
```python
assert page.url == "https://example.com/dashboard"
assert page.locator(".success-message").is_visible()
```

### Taking Screenshots
```python
page.screenshot(path="screenshot.png")
```

### Handling Frames
```python
frame = page.frame(name="iframe_name")
frame.click("button.submit")
```

### Handling Alerts
```python
page.on("dialog", lambda dialog: dialog.accept())
page.click("#confirmButton")
```

## 4. API Automation with Playwright
Playwright allows API testing using `request`.

### Sending a GET Request
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    print(response.status, response.json())
```

### Sending a POST Request
```python
response = request.post("https://jsonplaceholder.typicode.com/posts",
    data={"title": "foo", "body": "bar", "userId": 1})
print(response.status, response.json())
```

### Sending a PUT Request
```python
response = request.put("https://jsonplaceholder.typicode.com/posts/1",
    data={"id": 1, "title": "updated", "body": "bar", "userId": 1})
print(response.status, response.json())
```

### Sending a DELETE Request
```python
response = request.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status)
```

## 5. Playwright with Pytest
To integrate Playwright with Pytest, install pytest-playwright:
```sh
pip install pytest-playwright
```

### Example Pytest Test Case
```python
import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_login(page):
    page.goto("https://example.com/login")
    page.fill("#username", "test_user")
    page.fill("#password", "password123")
    page.click("#login")
    assert page.url == "https://example.com/dashboard"
```

## 6. Running Tests
Run tests using:
```sh
pytest -v test_script.py
```

For headed mode:
```sh
pytest --headed -v test_script.py
```

## 7. Parallel Execution
Enable parallel execution using:
```sh
pytest -n 3 --dist=loadscope
```

## 8. Playwright Codegen (Record and Generate Tests)
To generate test scripts automatically:
```sh
playwright codegen https://example.com
```

## 9. Browser Support
* Chrome
* Firefox
* Webkit


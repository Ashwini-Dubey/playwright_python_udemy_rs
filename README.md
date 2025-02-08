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

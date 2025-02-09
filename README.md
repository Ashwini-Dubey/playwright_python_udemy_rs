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

## 4.  List of Locators

### 1️⃣ `get_by_role()`
- Locates elements based on their **ARIA role** (e.g., `button`, `link`, `combobox`).
- **Best for:** Buttons, links, dropdowns, checkboxes, radio buttons, etc.
- **Example:**
  ```python
  page.get_by_role("button", name="Submit").click()
  ```

---

### 2️⃣ `get_by_label()`
- Finds form elements (`<input>`, `<textarea>`, `<select>`) based on their **associated label**.
- **Best for:** Input fields with labels.
- **Example:**
  ```python
  page.get_by_label("Username:").fill("test_user")
  ```

---

### 3️⃣ `get_by_placeholder()`
- Locates input elements using their `placeholder` attribute.
- **Best for:** Search bars, login forms with placeholder text.
- **Example:**
  ```python
  page.get_by_placeholder("Enter your email").fill("test@example.com")
  ```

---

### 4️⃣ `get_by_text()`
- Finds elements containing **visible text**.
- **Best for:** Locating buttons, links, or text elements based on their content.
- **Example:**
  ```python
  page.get_by_text("Forgot Password?").click()
  ```

---

### 5️⃣ `locator()`
- Finds elements using **CSS selectors or XPath**.
- **Best for:** Custom element selection when other locators don’t work.
- **Example:**
  ```python
  page.locator("#username").fill("test_user")  # Using CSS selector
  page.locator("//button[text()='Submit']").click()  # Using XPath
  ```

---

### 6️⃣ `get_by_test_id()`
- Selects elements using `data-testid` attributes (commonly used in test automation).
- **Best for:** Selecting elements with predefined test IDs.
- **Example:**
  ```python
  page.get_by_test_id("login-button").click()
  ```

---

### 7️⃣ `get_by_title()`
- Selects elements using the `title` attribute.
- **Best for:** Tooltips, icons, or elements with descriptive titles.
- **Example:**
  ```python
  page.get_by_title("Help").click()
  ```


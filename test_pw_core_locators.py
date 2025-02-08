import time

from playwright.sync_api import Page

def test_pw_core_locators(page:Page):
    # Launching the browser and opening the URL
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # Locating the Username field with the label
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")

    # Locating the Student/Teacher/Consultant dropdown with get_by_role("combobox")
    page.get_by_role("combobox").select_option("consult")






import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False,
            slow_mo=1000
        )  # Set headless=False to see the browser actions
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_contact_form(page):
    print("read in google")
    page.goto("https://obchod.aikidoprokazdeho.cz/")

# přijetí cookies 
    button = page.wait_for_selector(
        "body > div.siteCookies.siteCookies--bottom.siteCookies--dark.js-siteCookies > div > div.siteCookies__buttonWrap > button"
    )
    button.click()

# tlačítko zlevněné vstupné
    button1 = page.wait_for_selector(
        '#products-9 > div > div:nth-child(2) > div > div > div.p-bottom.single-button > div > div.p-tools > a'
    )
    button1.click()

# otevření formuláře pro komunikaci
    button2 = page.wait_for_selector(
        '#content > div > div.p-detail-inner > div.p-data-wrapper > div.buttons-wrapper.social-buttons-wrapper > div > a.link-icon.chat'
    )
    button2.click()

# ověření otevření formuláře pro komunikaci
    assert '#cboxLoadedContent > div', "formulář se neotevřel"

# vykřížkování formuláře
    button3 = page.wait_for_selector(
        '#cboxClose'
    )
    button3.click()
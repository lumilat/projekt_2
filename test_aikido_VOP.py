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

# přesměrování na Obchodní podmínky
    butoon2 =page.wait_for_selector(
        '#navigation > div > ul.menu-level-1 > li.menu-item-39 > a'
    )
    butoon2.click()

# ověření přesměrování na Obchodní podmínky
    assert page.title() == 'Obchodní podmínky - Aikido pro každého', "Obchodní podmínky nenalezeny"
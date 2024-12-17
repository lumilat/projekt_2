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

def test_google_search_result(page):
    query = "playwright"
    print("read in google")
    page.goto("https://www.google.com")

    print("Přijmout vše?")
    page.wait_for_selector('#L2AGLb', timeout=60000)
    button = page.query_selector('#L2AGLb')
    print("kliknutí na button")
    button.click()

    print("Waiting for search input")
    page.wait_for_selector('#APjFqb',timeout=60000)
   
    print("Filling search input")
    page.fill('#APjFqb', query)
    page.press('#APjFqb', "Enter")

    print("sign all results")
    page.wait_for_selector('a[jsname="UWckNb"]',timeout=600000)  # waits for the search results to load
    search_results = page.query_selector_all('a[jsname="UWckNb"]')  # retrieves all search result
   
    assert len(search_results) > 0, "No search results found"

    print(f"Number of search results: {len(search_results)}")
    assert query in search_results[0].inner_text(), "Search term not found in first result"
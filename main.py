from playwright.sync_api import sync_playwright
import time
URL = "https://www.next.co.uk/clearance/search?w=women&p=1&af=category:dresses%20gender:women%20size:10%20size:8&isort=price#0"


def main():
      with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()
        page.goto(URL, wait_until="networkidle", timeout=120000)

        print(page.title())

        browser.close()

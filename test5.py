from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        base_url='https://selenium.dunossauro.live/'
    )
    page.goto('aula_05_a.html')
    
    div = page.locator('div').nth(0)
    
    print(div.text_content())
    
    browser.close()
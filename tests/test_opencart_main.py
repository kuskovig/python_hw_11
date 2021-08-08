

def test_opens_mainpage_with_default_url(browser, url):
    browser.get(url)
    assert browser.title == "Your Store"


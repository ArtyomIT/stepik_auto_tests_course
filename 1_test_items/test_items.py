def test_add_item_to_box(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    butt_add = browser.find_element('xpath', '//form[@id = "add_to_basket_form"]//button[@type="submit"]')
    assert butt_add.is_displayed()


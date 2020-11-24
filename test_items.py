import time
def test_guest_should_see_button(language_opt, browser):
    link = f'http://selenium1py.pythonanywhere.com/{language_opt}' \
           f'/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements_by_class_name('btn-success')) == 1, \
        'The button is not found'

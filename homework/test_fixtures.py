from selene import browser, be


def test_github_desktop(browser_management_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login_field').should(be.visible)


def test_github_mobile(browser_management_mobile):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login_field').should(be.visible)

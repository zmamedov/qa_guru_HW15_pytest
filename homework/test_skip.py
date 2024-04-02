import pytest
from selene import browser, be


def test_github_desktop(browser_management):
    if browser_management == 'mobile':
        pytest.skip(reason='Разрешение сторон экрана для телефона')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login_field').should(be.visible)


def test_github_mobile(browser_management):
    if browser_management == 'desktop':
        pytest.skip(reason='Разрешение сторон экрана десктопное')

    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login_field').should(be.visible)

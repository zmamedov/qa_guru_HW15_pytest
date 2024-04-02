import pytest
from selene import browser, be

desktop_only = pytest.mark.parametrize("browser_management_desktop",
                                       [(1920, 1080), (1280, 720)],
                                       indirect=True,
                                       ids=['Full HD', 'HD'])
mobile_only = pytest.mark.parametrize("browser_management_mobile",
                                      [(414, 896)],
                                      indirect=True,
                                      ids=['IPhone XR'])


@desktop_only
def test_github_desktop(browser_management_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login_field').should(be.visible)


@mobile_only
def test_github_mobile(browser_management_mobile):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login_field').should(be.visible)

import pytest
from selene import browser


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 720), (2560, 1440)], ids=['Full HD', 'HD', '2K'])
def browser_management_desktop(request):
    browser.config.base_url = 'https://github.com'

    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(414, 896), (360, 740), (480, 854)],
                ids=['IPhone XR', 'Galaxy S8+', 'Nokia N9'])
def browser_management_mobile(request):
    browser.config.base_url = 'https://github.com'

    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 720), (414, 896)],
                ids=['Full HD', 'HD', 'IPhone XR'])
def browser_management(request):
    browser.config.base_url = 'https://github.com'

    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    if width > 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()

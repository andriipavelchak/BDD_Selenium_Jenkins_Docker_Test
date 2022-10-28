import pytest
import json
from pytest_bdd import given
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


# Hooks
# Represent "step" information in case of error
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Run one time before entire test suite
@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_files:
        config = json.load(config_files)

    # Assert values are acceptable
    assert config['browser'] in ['LocalFirefox', 'LocalChrome', 'LocalHeadlessChrome', 'LocalToRemoteChrome', 'RemoteToRemoteChrome']

    # Return config so it can be used
    return config


# Decorator. "browser" fixture depends on "config" fixture
@pytest.fixture
def browser(config):
    # Setup Phase. Run before test with particular fixture
    # Initialize the ChromeDriver instance
    if config['browser'] == 'LocalFirefox':
        b = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif config['browser'] == 'LocalChrome':
        b = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif config['browser'] == 'LocalHeadlessChrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        opts.add_argument('--log-level=1')
        b = webdriver.Chrome(options=opts)
    elif config['browser'] == 'LocalToRemoteChrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument("--headless")
        selenium_grid_url = "http://localhost:4444/wd/hub"
        b = webdriver.Remote(command_executor=selenium_grid_url, options=opts)
    elif config['browser'] == 'RemoteToRemoteChrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument("--headless")
        selenium_grid_url = "http://selenium-hub:4444/wd/hub"
        b = webdriver.Remote(command_executor=selenium_grid_url, options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Clean up Phase. Run automatically after pass or fail of test case
    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()

# @pytest.fixture
# def search_page(browser):
#     search_page = DuckDuckGoSearchPage(browser)
#     return search_page
#
# @pytest.fixture
# def result_page(browser):
#     result_page = DuckDuckGoResultPage(browser)
#     return result_page

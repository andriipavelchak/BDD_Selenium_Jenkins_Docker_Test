"""DuckDuckGo search tests"""
import time
import allure
from pytest_bdd import given, scenarios, then, when, parsers
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from utilities.inspect_methods import who_am_i

# import sys
# sys.path.append('..')

scenarios('../features/search.feature')


# Shared Given Steps
# First step used to reach page before running of each step. Located under Background in feature file
@given('the DuckDuckGo home page is displayed', target_fixture='ddg_home')
# Second Scenario for single search
@given('the DuckDuckGo home page is displayed', target_fixture='ddg_home')
def ddg_home(browser):
    global search_page
    global result_page
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    search_page.load()


@when(parsers.cfparse('the user searches for "{phrase}"'))
@when('the user searches for "<phrase>"')
def the_user_searches_for_phrase(phrase):
    search_page.search(phrase)


@then(parsers.cfparse('results are shown for "{phrase}"'))
@then('results are shown for "<phrase>"')
def results_are_shown_for_phrase(phrase):
    assert phrase == result_page.search_input_value()


@then(parsers.cfparse('search result links pertain to "{phrase}"'))
@then('search result links pertain to "<phrase>"')
def search_result_links_pertain_to_phrase(phrase):
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0


@then(parsers.cfparse('search result title contains "{phrase}"'))
@then('search result title contains "<phrase>"')
def search_result_title_contains_phrase(phrase):
    try:
        assert phrase in result_page.title()
    # Take a screenshot in case of error
    # Name consist of:
    # test_name part will take the function name
    # curr_time part will take current time of the problem
    except AssertionError as error:
        test_name = who_am_i.inspect_methods()
        curr_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(time.time()))
        screenshot_name = test_name + "_" + curr_time
        allure.attach(result_page.take_screenshot(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        raise error

"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By
from selenium import webdriver


class DuckDuckGoResultPage:

    # Locators

    RESULT_RELATED_LINKS = (By.CSS_SELECTOR, "a.result__a")
    SEARCH_INPUT = (By.ID, "search_form_input")

    # Initializer

    def __init__(self, browser):
        self.browser = browser
    # Interaction Methods


    def result_link_titles(self):
        # Plural
        links = self.browser.find_elements(*self.RESULT_RELATED_LINKS)
        # Return list of Strings not elements
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # Look for attribute name "value" and return
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title

    def take_screenshot(self):
        return self.browser.get_screenshot_as_png()

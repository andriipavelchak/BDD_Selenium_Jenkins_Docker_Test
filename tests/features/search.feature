Feature: Search DuckDuckGo
  As a web user, I want to find information in internet

  Scenario Outline: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "<phrase>"
    Then results are shown for "<phrase>"
    And search result links pertain to "<phrase>"
    And search result title contains "<phrase>"

    Examples: Phrases
      | phrase     |
      | python     |
      | selenium   |
      | pytest     |

  Scenario: Basic DuckDuckGo Search Single
    Given the DuckDuckGo home page is displayed
    When the user searches for "testing"
    Then results are shown for "testing"
    And search result links pertain to "testing"
    And search result title contains "12345"
Feature: Search Product
  As a user
  I want to search for products
  So that I can quickly find items I need

  @positive @basic
  Scenario: Search with exact product name
    Given I am on the search products page
    When I search for product "iPhone 16"
    Then I should see "iPhone 16" in the search results

  @positive @partial
  Scenario: Search with partial product name
    Given I am on the search products page
    When I search for product "apple"
    Then I should see products related to "apple"

  @positive @case-insensitive
  Scenario: Search with insensitive case
    Given I am on the search products page
    When I search for product "iphone"
    Then I should see products related to "iPhone"

  @positive @whitespace
  Scenario: Search with leading and trailing spaces
    Given I am on the search products page
    When I search for product "   iPhone   "
    Then I should see products related to "iPhone"

  @negative @empty
  Scenario: Search with empty input
    Given I am on the search products page
    When I search for product with empty value then verify alert

  @negative @notfound
  Scenario: Search with non-existing product
    Given I am on the search products page
    When I search for product "abcdefxyz"
    Then I should see no result message

  @negative @special-chars
  Scenario: Search with special characters
    Given I am on the search products page
    When I search for product "!@#$%^&*"
    Then I should see no result message

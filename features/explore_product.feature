Feature: Explore and filter products
  As a user
  I want to browse products by categories, sort, and apply filters
  So that I can quickly find items that match my needs

  @category @navigation
  Scenario: Navigate to Notebooks under Computers category
    Given I am on the homepage
    When I navigate to "Computers" category
    And I click "Notebooks"
    Then I should see a list of products under "Notebooks"

  @sort @price
  Scenario: Sort products by price (Low to High)
    Given I am on the homepage
    When I navigate to "Computers" category
    And I click "Notebooks"
    When I sort products by "Price: Low to High"
    Then the products should be displayed in ascending order of price
    

  @sort @price
  Scenario: Sort products by price (Low to High)
    Given I am on the homepage
    When I navigate to "Computers" category
    And I click "Notebooks"
    When I sort products by "Price: High to Low"
    When I Sleep for "1" seconds 
    Then the products should be displayed in descending order of price 

  @filter @manufacturer
  Scenario: Filter products by a specific manufacturer
    Given I am on the homepage
    When I navigate to "Computers" category
    And I click "Notebooks"
    When I filter products by manufacturer "Apple"
    Then only "Apple" products should be shown

  @filter @manufacturer
  Scenario Outline: Filter products by multiple manufacturers
    Given I am on the homepage
    When I navigate to "Computers" category
    And I click "Notebooks"
    When I filter products by manufacturer "<manufacturer>"
    Then only "<manufacturer>" products should be shown

    Examples:
      | manufacturer |
      | Apple        |
      | HP           |

  @filter @price
  Scenario: Filter products by a price range
    Given I am on the homepage
    When I navigate to "Computers" category
    And I click "Desktops"
    When I set the price filter from "200" to "1100"
    Then only products with price between "500" and "1000" should be shown

  @filter @price @edge
  Scenario: Filter products with no results
    Given I am on the homepage
    When I navigate to "Computers" category
    And I click "Desktops"
    When I set the price filter from "9800" to "10000"
    Then I should see no products available message

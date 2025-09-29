Feature: User Registration

  Scenario: Successful registration with random yopmail
    Given I am on the registration page
    When I register with a random yopmail
    Then I should see the registration success message
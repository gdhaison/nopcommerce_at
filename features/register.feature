Feature: User Registration

  @register @happy
  Scenario: Successful registration with random yopmail
    Given I am on the registration page
    When I register with a random yopmail
    Then I should see the registration success message

  @register @unhappy
  Scenario: Registration with existing email
    Given I am on the registration page
    When I register with an existing email "gdhaison@yopmail.com"
    Then I should see an error message "The specified email already exists"

  @register @unhappy
  Scenario: Registration with invalid email format
    Given I am on the registration page
    When I register with email "gdhaison!yopmail.com"
    Then I should see an error message from email field "Please enter a valid email address."

  @register @unhappy
  Scenario: Registration with password shorter than 6 characters
    Given I am on the registration page
    When I register detail with email "gdhaison@yopmail.com" and first name "Son" and last name "Vu" and password "123" and confirm password "123"
    Then I should see an error message from password field "Password must meet the following rules: must have at least 6 characters and not greater than 64 characters"

  @register @unhappy
  Scenario: Registration with mismatched passwords
    Given I am on the registration page
    When I register detail with email "gdhaison@yopmail.com" and first name "Son" and last name "Vu" and password "123456" and confirm password "654321"
    Then I should see an error message from password field "The password and confirmation password do not match."

  # @register @unhappy @flaky
  # Scenario: Registration with empty required fields
  #   Given I am on the registration page
  #   When I click register without filling any fields
  #   Then I should see required field validation errors

  # @edge
  # Scenario: Registration with email containing special characters
  #   Given I am on the registration page
  #   When I register with email "test+alias@yopmail.com"
  #   Then I should see the registration success message

  # @edge
  # Scenario: Registration with leading/trailing spaces in email
  #   Given I am on the registration page
  #   When I register with email "  testuser@yopmail.com  "
  #   Then I should see the registration success message

  # @edge
  # Scenario: Registration with password containing special characters
  #   Given I am on the registration page
  #   When I register with password "P@ssw0rd!#"
  #   Then I should see the registration success message

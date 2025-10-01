Feature: Forgot Password Functionality

  @forgot_pass @happy
  Scenario: User requests password reset with valid email
    Given I am on the forgot password page
    When I enter an email address "gdhaison@yopmail.com"
    And I click on RECOVER
    Then I should see a message "Email with instructions has been sent to you."
    When I open a new tab
    And I go to website "https://yopmail.com/"
    And I input email "gdhaison"
    And I click button search mail
    Then email from nopcommerce should be visible
    # send email feature is disable foe this website so couldnt check anymore

  @forgot_pass @unhappy
  Scenario: User requests password reset with invalid email
    Given I am on the forgot password page
    When I enter an email address "invalidemail@example.com"
    And I click on RECOVER
    Then I should see a message "Email not found."

  @forgot_pass @unhappy
  Scenario: User requests password reset with empty email field
    Given I am on the forgot password page
    When I click on RECOVER
    Then I should see an email error message "Enter your email"

#   Scenario: User requests password reset with email address not registered
#     Given I am on the login page
#     When I click on "Forgot password?"
#     And I enter a non-registered email address "nonuser@example.com"
#     And I click on "Recover"
#     Then I should see an error message "No account found with that email address."

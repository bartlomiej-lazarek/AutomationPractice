Feature: Login to portal

  @base_page @authentication_page
  Scenario: Log in using valid data
    When I open authentication page
    And login with username 'tester@tester.pl' and password 'tester'
    Then I verify that I successfully logged in by checking account name

  @base_page @authentication_page
  Scenario: Log in using invalid data
    When I open authentication page
    And login with username 'tester@tester.pl' and password 'tester123'
    Then I verify that I unsuccessfully logged in by checking error message

  @base_page @authentication_page
  Scenario: Log in with empty email field
    When I open authentication page
    And login with empty username and password 'tester123'
    Then Verify error message contains 'An email address required'

  @base_page @authentication_page
  Scenario: Log in with empty password field
    When I open authentication page
    And login with empty username 'tester@tester.pl' and empty password
    Then Verify error message contains 'Password is required.'
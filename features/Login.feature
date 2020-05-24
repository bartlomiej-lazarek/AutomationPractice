Feature: Login to portal

  Scenario: Log in using valid data
    When I open authentication page
    And login with username 'tester@tester.pl' and password 'tester'
    Then I verify that I successfully logged in by checking account name

  Scenario: Log in using invalid data
    When I open authentication page
    And login with username 'tester@tester.pl' and password 'tester123'
    Then I verify that I unsuccessfully logged in by checking error message
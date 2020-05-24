Feature: Login to portal

  Scenario: Log in using valid data
    When I open authentication page
    And login with username 'tester@tester.pl' and password 'tester'
    Then I verify that I successfully logged in by checking account name
Feature: Search product on page

  Scenario: Search with empty value
    When I click on search input
    And I left search empty and press 'Enter'
    Then I see message Please enter a search keyword

  Scenario: Search with 'Printed' phrase
    When I click on search input
    And I enter 'Printed' and press 'Enter'
    Then I see only products witch name contains 'Printed'
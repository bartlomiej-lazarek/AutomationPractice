Feature: Search product on page

  @home_page
  Scenario: Search with empty value
    When I search for empty value
    Then I see message Please enter a search keyword

  @home_page
  Scenario: Search with 'Printed' phrase
    When I search for 'Printed'
    Then I see only products witch name contains 'Printed'
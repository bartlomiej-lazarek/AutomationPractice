Feature: Register new account in portal

  Scenario Outline: Register new account
    When I open authentication page
    And I set <email> address, next I click Create an account button
    And I set <title>, <name>, <last_name>, <password>, <address>, <city>, <postal_code>, <phone>, next I click Register button
    Then I should <result> register new account

    Examples: using valid data
      |email|title|name|last_name|password|address|city|postal_code|phone|result|
      |valid@email.com|MR|Jan|Kowalski|123123|Testowa 10|Bydgoszcz|12312|123123123|successfully|

    Examples: using valid data but all fields aren't filled
      |email|title|name|last_name|password|address|city|postal_code|phone|result|
      |valid@email.com|MR|Jan|Kowalski|empty|Testowa 10|empty|12312|123123123|unsuccessfully|

    Examples: using invalid data
      |email|title|name|last_name|password|address|city|postal_code|phone|result|
      |valid@email.com|MR|5125|Kowalski|123123|Testowa 2|1012312|21345|asd|unsuccessfully|


  Scenario: Register using invalid email
    When I open authentication page
    And I set email 'invalid@', next I click Create an account button
    Then I verify that error message contains: Invalid email address
Feature: Register new account in portal

  Scenario Outline: Register new account
    When I open authentication page
    And I set <email> address, next I click Create an account button
    And I set <title>, <name>, <last_name>, <password>, <address>, <city>, <phone>, next I click Register button
    Then I <result> register new account

    Examples: using valid data
      |email|title|name|last_name|password|address|city|phone|result
      |val21id@email.com|MR|Jan|Kowalski|123123|Testowa 10|Bydgoszcz|123123123|successfully

    Examples: using invalid email
      |email|title|name|last_name|password|address|city|phone|result
      |invalidemail@|MR|Jan|Kowalski|123123|Testowa 10|Bydgoszcz|123123123|unsuccessfully

    Examples: using valid data but all fields aren't filled
      |email|title|name|last_name|password|address|city|phone|result
      |valide514@email.com|MR|Jan|Kowalski||Testowa 10||123123123|unsuccessfully

    Examples: using invalid data
      |email|title|name|last_name|password|address|city|phone|result
      |validem451@email.com|MR|5125|Kowalski||Testowa 10||abcd|unsuccessfully


  Scenario: Register using valid data
    When I open authentication page
    And I set valid email address, next I click Create an account button
    And I set all required fields, next I click Register button
    Then I verify that I successfully registered by checking logged account name

  Scenario: Register using invalid email
    When I open authentication page
    And I set invalid email, next I click Create an account button
    Then I verify that error message contains: Invalid email address

  Scenario: Register using valid data but all fields aren't filled
    When I open authentication page
    And I set valid email address, next I click Create an account button
    And I set all fields except: password, city
    Then I verify that error message contains: 'There are 2 errors 1. passwd is required. 2. city is required.'

  Scenario: Register using invalid data
    When I open authentication page
    And I set valid email address, next I click Create an account button
    And I set all required fields, but as first name I set '123' and phone 'asd'
    Then I verify that error message contains: 'There are 2 errors 1. firstname is invalid. 2. phone is invalid.'
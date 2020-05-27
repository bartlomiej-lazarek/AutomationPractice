Feature: Register new account in portal

  Scenario Outline: Register new account
    When I open authentication page
    And I set <email> address, next I click Create an account button
    And I set <title>, <name>, <last_name>, <password>, <address>, <city>, <postal_code>, <phone>, next I click Register button
    Then I should <result> register new account

    Examples: using valid data
      |email|title|name|last_name|password|address|city|postal_code|phone|result|
      |valdadsadasdsa21id@email.com|MR|Jan|Kowalski|123123|Testowa 10|Bydgoszcz|12312|123123123|successfully|

    Examples: using invalid email
      |email|title|name|last_name|password|address|city|postal_code|phone|result|
      |invalidemail@|MR|Jan|Kowalski|123123|Testowa 10|Bydgoszcz|12312|123123123|unsuccessfully|

    Examples: using valid data but all fields aren't filled
      |email|title|name|last_name|password|address|city|postal_code|phone|result|
      |valide514@email.com|MR|Jan|Kowalski||Testowa 10||12312|123123123|unsuccessfully|

    Examples: using invalid data
      |email|title|name|last_name|password|address|city|postal_code|phone|result|
      |validem451@email.com|MR|5125|Kowalski|123123|Testowa 2|1012312|21345|asd|unsuccessfully|



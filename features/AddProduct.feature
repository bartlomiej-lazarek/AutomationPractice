Feature: Add product to cart

  Scenario: Add product to cart using button on hover on product
    When I hover on first product on page
    And I click Add to cart button
    Then Should be displayed message Product successfully added to your shopping cart


  Scenario: Add product to cart using quick view
   When I hover on first product on page
   And I click Quick view button
   And I click Add to cart button on quick view
   Then Should be displayed message Product successfully added to your shopping cart


  Scenario: Add product to cart from product page
    When I click on first product on page
    And I click Add to cart button on product page
    Then Should be displayed message Product successfully added to your shopping cart

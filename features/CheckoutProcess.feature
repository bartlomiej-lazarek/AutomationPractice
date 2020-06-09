Feature: Checkout Process
  Scenario: Purchase product by logged user using Pay by bank wire
    Given Login with username 'tester@tester.pl' and password 'tester'
    When I go to Home Page
    And I click on first product on page
    And I click Add to cart button on product page
    And I click Proceed to checkout and go to Cart
    And I click Proceed to checkout and go to Address step
    And I click I click Proceed to checkout and go to Shipping step
    And I click checkbox Terms of service
    And I click Proceed to checkout and go to Payment step
    And I click Pay by bank wire
    And I click confirm my order
    Then Should be displayed information that order is complete


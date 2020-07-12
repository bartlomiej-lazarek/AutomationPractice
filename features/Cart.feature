Feature: Operation in shopping cart

  @home_page @base_page @summary_page
  Scenario Outline: Check total products price
    When I add <products_qty> random products to cart
    And I go to cart
    Then Total products price should be equal to sum all unit products price in cart

      Examples:
        |products_qty|
        |1           |
        |3           |
        |5           |

  @home_page @base_page @summary_page
  Scenario: Change product qty in a cart by icons
    When I click on first product on page
    And I click Add to cart button on product page
    And I click Proceed to checkout and go to Cart
    And I click '+' icon in qty field
    Then Products qty should be 2
    And Total products price should be 2 times bigger

  @home_page @base_page @summary_page
  Scenario: Change product qty in a cart by input
    When I click on first product on page
    And I click Add to cart button on product page
    And I click Proceed to checkout and go to Cart
    And I click in Qty input field and set 2
    Then Products qty should be 2
    And Total products price should be 2 times bigger
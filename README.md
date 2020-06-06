# AutomationPractice
This is project for learning test automation in Python3 using Selenium Webdriver and Behave BDD.  
Tests have written for http://automationpractice.com/index.php

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Downlaod repository
```
git clone https://github.com/bartlomiej-lazarek/AutomationPractice.git
```

### Installing requirements
```
pip3 install -r requirements.txt
```
To run Allure you have to install Java JDK (https://openjdk.java.net/install) and set JAVA_HOME.


### Run tests
Use command below in main project folder.
```
behave
```

#### Example output:

```
Scenario: Add product to cart from product page                                     # features/AddProduct.feature:16
    When I click on first product on page                                             # features/steps/add_product_steps.py:38
    And I click Add to cart button on product page                                    # features/steps/add_product_steps.py:44
    Then Should be displayed message Product successfully added to your shopping cart # features/steps/add_product_steps.py:18  

4 features passed, 0 failed, 0 skipped
13 scenarios passed, 0 failed, 0 skipped
41 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m41.839s
```


### Run tests with Allure report
This command will start tests. Results will be save in allure/results directory as json files.
```
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features
```
This command will generate Allure report based on previously generated results.
```
allure generate allure/results/ -o allure/reports
```
This command will open Allure web page with the test report.
```
allure open allure/reports
```

#### Example output:
![Allure report 1](https://i.imgur.com/TFTSsis.png)
![Allure report 2](https://i.imgur.com/bmxygcM.png)
![Allure report 3](https://i.imgur.com/ezByie8.png)


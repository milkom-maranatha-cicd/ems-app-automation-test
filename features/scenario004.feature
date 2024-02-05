Feature: Scenario 004
  Scenario: Login with valid credentials, validate initial and updated employee dataset, delete employee, and logout
    Given I am on the sign in page
    When I login with valid credentials
    Then I should be on the dashboard page
    And the table dataset should be initially empty or match the predefined data
    When I delete the first employee
    Then the table dataset must not contain the deleted employee
    When I logout from the system
    Then I should be back on the sign in page

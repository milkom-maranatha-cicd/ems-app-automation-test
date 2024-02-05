Feature: Scenario 002
  Scenario: Login with valid credentials, validate initial and updated employee dataset, add new employee, and logout
    Given I am on the sign in page
    When I login with valid credentials
    Then I should be on the dashboard page
    And the table dataset should be initially empty or match the predefined data
    When I open the add employee page
    Then I should be on the add employee page
    And the add employee page should have the required properties
    When I save a new employee with the details
      | first_name  | last_name      | email               | salary | date       |
      | Added       | New Employee   | new@employee.com    | 20000  | 05/12/2023 |
    Then the table dataset should contain the new employee
    When I logout from the system
    Then I should be back on the sign in page

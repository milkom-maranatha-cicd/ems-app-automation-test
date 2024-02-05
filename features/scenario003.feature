Feature: Scenario 003
  Scenario: Login with valid credentials, validate initial and updated employee dataset, edit the first employee, and logout
    Given I am on the sign in page
    When I login with valid credentials
    Then I should be on the dashboard page
    And the table dataset should be initially empty or match the predefined data
    When I edit the first employee
    Then I should be on the edit employee page
    When I save the edited employee with the details
      | first_name  | last_name      | email                    | salary | date       |
      | John        | Edited         | susan-edited@mail.com    | 20000  | 05/12/2023 |
    Then the table dataset should contain the edited employee
    When I logout from the system
    Then I should be back on the sign in page

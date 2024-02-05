Feature: Login Scenario 001

  Scenario: Login with valid credentials, validate employee dataset, and logout
    Given I am on the sign in page
    When I login with valid credentials
    Then I should be on the dashboard page
    And I should see the table headers
    And the table content should match the predefined data
    When I logout from the system
    Then I should be back on the sign in page

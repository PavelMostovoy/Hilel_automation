# Created by pmostovoi at 5/19/22
Feature: Second Feathure
  # Enter feature description here

  Scenario Outline: Name Comparison
    Given User '<name>'
    When Add additional user '<name_1>'
    Then Compare Users names
    Examples:
      | name | name_1 |
      | Bob  | Bob    |
      | Bill | Mike   |
      | Mike | Mike   |
      | Bob  | Mike   |

  Scenario Outline: Test login user
    Given User '<name>'

    When User send Get request to <url>
    Then Check response <code>

    Examples:
      | name | data | User_1 | browser | browser_1 | url         | code   |
      | Bill | 123  | Tim    | chrome  | chrome    | https://www | 200 |
      | Timm | 2456 | Nic    | chrome  | firefox   | https://www | 403|
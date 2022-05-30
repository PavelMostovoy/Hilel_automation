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

#  Scenario Outline: Test login user
#    Given User '<name>'
#    And User_1 '<User_1>'
#
#    When <name> open <url> using browser <browser>
#    And <User_1> open <url_1> using browser <browser_1>
#    And User fill <data> in form
#    And User_1 Delete <data> from form
#
#
#    Then User can't see <data> in ...
#
#    Examples:
#      | name | data | User_1 | browser | browser_1 | url         | url_1   |
#      | Bill | 123  | Tim    | chrome  | chrome    | https://www | http:// |
#      | Timm | 2456 | Nic    | chrome  | firefox   | https://www | http:// |
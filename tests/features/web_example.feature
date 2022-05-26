# Created by pmostovoi at 5/19/22
Feature: First test
  # Enter feature description here

  Scenario: Login on page
    Given User 'Bill'
    When Add additional user 'Bill'
    Then Compare Users names
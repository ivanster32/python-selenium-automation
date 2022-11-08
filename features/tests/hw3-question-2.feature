# Created by ivansantana at 11/8/22
Feature: sign in test case
  # Enter feature description here

  Scenario: user must sign in
    Given open amazon page
    When click on orders
    Then verify the sign in page is open


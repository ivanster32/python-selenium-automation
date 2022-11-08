# Created by ivansantana at 11/7/22
Feature: Test for amazon Search
  # Enter feature description here

  Scenario: User can search for a product on amazon
    Given open amazon page
    When search for the coffee
    Then Search results for coffee are shown


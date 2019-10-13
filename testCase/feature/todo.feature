# Created by harshit at 7/7/2019
Feature: REST API testing framework using using BDD approach with pytest and behave
  Raise request(s) using responses
  Validate HTTP response code and parse JSON response
  Make sure to run the intended REST API based web application as pre-condition

  Background:
    Given Set application url is "http://localhost:5000/tasks"
    And Set task details as "<paramKey>" and "<paramValue>" below
      | paramKey        | paramValue   |
      | task_name       | aquaApi      |
      | complete_status | false        |
      | new_task_name   | 12aqauapi300 |

#  Scenario: GET request for correct id
#    Given Set GET api endpoint as "bxPP1p4H"
#    When Set HEADER param request content type as "application/json"
#    And Set HEADER param response accept type as "application/json"
#    When Raise "GET" HTTP request
#    Then Valid HTTP response should be received
#    And Response http code should be 200
#    And Response HEADER content type should be "application/json"
#
#
  Scenario: POST request example
    Given Set POST api endpoint as "x10aquaQA"
    When Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
    And Set BODY form param using Set task details
    And Raise "POST" HTTP request
    Then Valid HTTP response should be received
    And Response http code should be 200
    And Response HEADER content type should be "application/json"
    And Response BODY should not be null or empty

#  Scenario: PUT request example
#    # I have ued POST request data to in PUT request instead of creating new data to for PUT
#    Given Set PUT api endpoint as "fruUCp2R"
#    When Set HEADER param request content type as "application/json"
#    And Set HEADER param response accept type as "application/json"
#    And Modify BODY form param using Set task details
#    And Raise "PUT" HTTP request
#    Then Valid HTTP response should be received
#    And Response http code should be 200

  Scenario: DELETE request example
    Given Set DELETE api endpoint as "bxPP1p4H"
    And Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
    And Raise "DELETE" HTTP request
    Then Valid HTTP response should be received
    And Response http code should be 200
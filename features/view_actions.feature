Feature: View Actions
	In order to know what's happening in my game
	As a player
	I want to view all actions that happened in my game

Scenario: View Actions by game id and day
	Given "1" games exist
	And "1" actions exist
	When the actions are viewed by game and time "1"
	Then the actions are returned
	
Scenario: View Actions by game id with 5 actions
	Given "1" games exist
	And "5" actions exist
	When the actions are viewed by game
	Then the actions are returned

Scenario: View Actions by game id and day with a day with no actions
	Given "1" games exist
	And "1" actions exist
	When the actions are viewed by game and time ""
	Then the actions are returned

Scenario: View Actions by game id and day with an invaild day
	Given "1" games exist
	And "1" actions exist
	When the actions are viewed by game and time "-1"
	Then the actions are returned

Scenario: View Actions by game id with an invalid game id
	Given "1" games exist
	And "1" actions exist
	When the actions are viewed by invalid game
	Then the actions are returned
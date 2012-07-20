Feature: View Game
	In order to decide whether or not I want to register
	As a User
	I want to view the specifics about a game

Scenario: Game with only one player
	Given "1" games exist
	And "1" players exist
	When the game is viewed
	then the game is returned

Scenario: Game with eight player
	Given "1" games exist
	And "8" players exist
	When the game is viewed
	Then the game is returned
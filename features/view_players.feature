Feature: View Players
	In order to know who's in a game
	As a player
	I want to view all players names, user ids, and if they're alive or not

Scenario: View Players when 1 game
	Given "1" games exist
	And "1" players exist
	When the players are viewed
	Then the players are returned
	

Scenario: View Players with 9 players in 1 game
	Given "1" games exist
	And "9" players exist
	When the players are viewed
	Then the players are returned

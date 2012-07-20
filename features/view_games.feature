Feature: View Games
	In order to pick a game to view
	As a user
	I want to view all available games

Scenario: View Games when 1 game
	Given "1" games exist
	When the games are viewed
	Then the games are returned


Scenario: View Games with 300 games
	Given "9" games exist
	When the players are viewed
	Then the players are returned

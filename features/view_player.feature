Feature: View Player
	In order to judge a player
	As a player
	I want to view their id, userid, name, and voting history

Scenario: View Player By ID
	Given "1" players exist
	When the player is viewed
	Then the player is returned


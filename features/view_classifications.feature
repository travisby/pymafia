Feature: View Classifications
	In order to see what classifications are implimented
	As a player
	I want to view all available classes with their alignments and skills

Scenario: View all classifications when 1 exist
	Given "1" classifications exist
	When the classifications are viewed
	Then the classifications are returned

Scenario: View all classifications when 3 exist
	Given "3" classifications exist
	When the classifications are viewed
	Then the classifications are returned

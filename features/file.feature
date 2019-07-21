Feature: Saving and comparing text files

	Scenario: Writing to a file
		Given a list of comics and their information
		Then a file should successfully be written to

	Scenario: Loading a file
		Given a file
		Then that file should be loaded not be null
Feature: Counting the number of comics in total in the dashboard
	
	Scenario: Pagination correct
		Given a loaded dashboard
		Then the correct number of pages are calculated

	Scenario: Counting comics
		Given comics are on the page
		Then the number of comics should be greater than 0

	Scenario: Counting all comics
		Given the latest comic number
		Then the latest comic number should equal total the number of comics
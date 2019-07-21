Feature: Counting the number of comments on a comic page

	Scenario: Finding comments on an uncommented page
		Given an uncommented loaded page
		Given a page has no comments
		Then number of comments should be 0

	Scenario: Finding comments
		Given a loaded page
		Then we should look for comments
		And number of comments should be greater than 0

	Scenario: Returning the page
		Given a comic and a returned page
		Then the name shouldn't be blank
		And the number of comments should be 0 or more
		And the url shouldn't be blank


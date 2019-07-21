from icecream import ic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

from comicPage import ComicPage

import collections
import json


class Dashboard(object):
	"""
		Use JSON for data structure?
		
		If document of URLs exist,
			Navigate to dashboard of comic
			Calculate how many comics are present
			If number of rows in document are the same as number of comments
				commentCounting()
			Else
				For each new comic number,
					Take the link and prepend them on to the document with numberOfComments = 0.

		Else if no document exists,
			Navigate to dashboard of comic.
			For each comic
					Take the link and prepend them on to the document with numberOfComments = 0.
			If pages remaining,
				Navigate to next page of comics.	
			Else
				commentCounting()


		commentCounting()
			For each link,
				Go into each comic page and get the number of comments.
				Compare with document for each comment
				If number of comments == numberOfComments
					Exit
				Else
					Save that row into a list
					Update the document
			Print the results

		Proof of concept:

			Navigate to dashboard.
			Get ONE link and save it into a list.
		
		Proof of concept (version 2):
			Get all comics url from current page.
			Move to next page
			Repeat
	"""

	url = ""
	driver = ""
	currentPage = 1
	comicURLs = collections.deque()

	latestComic = 0	
	paginationURLs = []

	comics = []

	def __init__(self, driver):
		self.driver = driver
		

	def getDashboard(self, url):
		self.driver.get(url)	

	def getLatestComicNumber(self):
		firstElement = self.driver.find_element_by_xpath("//li[contains(@id, 'episode_')]")
		latestComic = int(firstElement.get_attribute("data-episode-no"))
		return latestComic

	def countComicsOnPage(self):
		counter = ComicPage(self.driver)
		time.sleep(.3)
		elements = self.driver.find_elements_by_xpath("//a[contains(@href, 'episode_')]")
		for element in elements:
			elementID = element.get_attribute("id")
			# Special case to make sure the "First Episode" and previously read comics are added to deque.
			if elementID not in ("_btnEpisode", "continueRead"):
				self.comicURLs.appendleft(element.get_attribute("href"))
		return self.comicURLs

	def pageNavigation(self):
		self.paginationURLs.append(self.driver.current_url)

		numberOfPages = self.driver.find_element_by_css_selector("div[class=paginate]")
		links = numberOfPages.find_elements_by_css_selector("a")
		
		while (self.currentPage != len(links)):
			url = links[self.currentPage].get_attribute("href")
			self.paginationURLs.append(url)
			self.currentPage = self.currentPage + 1

		return self.paginationURLs

	def countUpAllComics(self):
		for link in self.paginationURLs:
			if link == self.driver.current_url:
				self.countComicsOnPage()
			else:
				self.driver.get(link)
				self.countComicsOnPage()
		return self.comicURLs

	def resetDashboard(self):
		self.comicURLs.clear()


	def countAllComments(self):
		for comic in self.comicURLs:
			counter = ComicPage(self.driver)
			counter.getComic(comic)
			test = counter.commentCounting()

			self.comics.append(test)

	def writeToFile(self):
		# Change this, write urls and comment count to file
		with open("links.json", "w") as f:
			json.dump(self.comics, f, indent=4)
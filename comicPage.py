from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import json
from icecream import ic

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Actions(ActionChains):
    def wait(self, time_s: float):
        self._actions.append(lambda: time.sleep(time_s))
        return self


class ComicPage(object):

	driver = []

	def __init__(self, driver):
		self.driver = driver
		# Things to do 
		# Deal with null pages
		# Deal with paginated comments
		# Each comic page has a title, URL, and comment count
		# Dump info on each comic page into JSON (overload print and comparison methods)
		#
		#
		# Wait until comment boxes are loaded on to the page.
		# For every comment with a reply toggle, move to it and click it.
		# Find all the comments, then tally them up.

	def getComic(self, url):
		self.driver.get(url)	

	def commentCounting(self):
		page = {
			"Name": "",
			"Number of comments": "",
			"URL": ""
		}
		try:	
			if (WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_comment_box")))):
				self.openingReplies()
				replies = self.driver.find_elements_by_xpath("//span[contains(@class, 'u_cbox_contents')]")
				sep = " |"
				title = self.driver.title.split(sep, 1)[0]	
				page["Name"] = title
				page["Number of comments"] = len(replies)
				page["URL"] = self.driver.current_url

				return page
		except TimeoutException:
			sep = " |"
			title = self.driver.title.split(sep, 1)[0]
			page["Name"] = title
			page["Number of comments"] = 0
			page["URL"] = self.driver.current_url
			return page

	def openingReplies(self):
		elements = []
		replyButtons = self.driver.find_elements_by_css_selector("a[data-action='reply#toggle']")
		for button in replyButtons:
			dataParam = "a[data-param='" + button.get_attribute("data-param" ) + "']"
			elements.append(dataParam)

		for css_selector in elements:
			actions = Actions(self.driver)
			button = self.driver.find_element_by_css_selector(css_selector)
			ic(css_selector + ": " + str(button))
			actions.move_to_element(button)
			actions.click()
			actions.perform()
			time.sleep(.5)
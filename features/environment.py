from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
sys.path.append('..\\')

from jsonParser import jsonParser
from comicPage import ComicPage
from dashboard import Dashboard

def before_all(context):
	context.browser = webdriver.Chrome("..\\Drivers\\chromedriver")
	context.cp = ComicPage(context.browser)
	context.dash = Dashboard(context.browser)
	j = jsonParser()
	settings = j.readJSON(path="../../lineniumSettings.json")
	context.url = settings["comicURL"]
	context.noCommentURL = settings["noCommentURL"]
	context.commentsURL = settings["commentsURL"]

def after_all(context):
	context.browser.quit()

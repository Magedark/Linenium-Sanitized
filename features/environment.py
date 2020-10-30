from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from icecream import ic
from dotenv import load_dotenv, find_dotenv



sys.path.append('..\\')

from jsonParser import jsonParser
from comicPage import ComicPage
from dashboard import Dashboard

def before_all(context):
	options = Options()
	options.headless = True

 #    chrome_options.add_argument("--headless")
 #    chrome_options.add_argument("--no-sandbox")
 #    chrome_options.add_argument("--disable-dev-shm-usage")
 #    chrome_prefs = {}
 #    chrome_options.experimental_options["prefs"] = chrome_prefs
 #    chrome_prefs["profile.default_content_settings"] = {"images": 2}
# driver = webdriver.Chrome(ChromeDriverManager().install())

	context.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
	context.cp = ComicPage(context.browser)
	context.dash = Dashboard(context.browser)
# https://stackoverflow.com/questions/49770999/docker-env-for-python-variables
	# If .env file is present, read from those values.
	# Only load if test env file is present (test.env)
	load_dotenv(find_dotenv())

	context.url = os.getenv("COMIC_URL")
	context.noCommentURL = os.getenv("NO_COMMENT_URL")
	context.commentsURL = os.getenv("COMMENTS_URL")
	ic(context.url)

def after_all(context):
	context.browser.quit()

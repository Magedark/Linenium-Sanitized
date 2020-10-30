from selenium import webdriver
from comicPage import ComicPage
from dashboard import Dashboard
from jsonParser import jsonParser
from webdriver_manager.chrome import ChromeDriverManager


def mainDashboard():
	# options = Options()
	# options.headless = True
	# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
	# j = jsonParser()
	# settings = j.readJSON()
	# print(settings["comicURL"])
	# url = settings["comicURL"]
	# d = Dashboard(driver)
	# d.getDashboard(url)
	# d.pageNavigation()
	# d.countUpAllComics()
	# d.countAllComments()
	# d.writeToFile()

mainDashboard()
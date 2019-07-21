from selenium import webdriver
from comicPage import ComicPage
from dashboard import Dashboard
from jsonParser import jsonParser

def mainDashboard():
	driver = webdriver.Chrome("Drivers\\chromedriver")
	j = jsonParser()
	settings = j.readJSON()
	print(settings["comicURL"])
	url = settings["comicURL"]
	d = Dashboard(driver)
	d.getDashboard(url)
	d.pageNavigation()
	d.countUpAllComics()
	d.countAllComments()
	d.writeToFile()

mainDashboard()
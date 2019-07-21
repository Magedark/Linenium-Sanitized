import json


class jsonParser(object):
	def __init__(self):
		pass

	def readJSON(self, path="../lineniumSettings.json"):
		with open(path) as json_file:
		    data = json.load(json_file)
		    return data

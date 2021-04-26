import os
import sys
import json

# run the code in the project
def runProject():
	jsonfile = open("config.json")
	jsonfile = json.load(jsonfile)
	mainfilename = jsonfile["mainfile"]
	mainfilename = mainfilename.split(".")[0]
	os.chdir("src")
	os.chdir(jsonfile["modulename"])
	os.system(f"java {mainfilename}.java")

import sys
import os

# Initilizes the java file
def initilizeJAVA(filename, packageName):
	javafile = open(filename, "w+")
	java_code = [f"package {packageName}.src.{packageName};", f"public class {filename.split('.')[0]}" + "{", "	public static void main(String[] args){","	}" ,"}"]
	for i in java_code:
		javafile.write(f"{i}\n")

# Edit the JSON file
def editJSON(mainfilename):
	jsonfile = open("config.json", "w+")
	jsoncode = ["{", f"	\"mainfile\" : \"{mainfilename}\"",  "}"]
	for i in jsoncode:
		jsonfile.write(f"{i}\n")

# The main function to create a new java project
def createJavaProject(project_name, package_name, main_file_name):
	filename = main_file_name.split('.')[0]
	commands_run = [f"mkdir {project_name}",
	 f"mkdir {project_name}/bin {project_name}/src", 
	 f"mkdir {project_name}/src/{package_name}", 
	 f"touch {project_name}/src/{package_name}/{filename}.java", 
	 f"mkdir {project_name}/bin/{package_name}", 
	 f"touch {project_name}/config.json"]
	for i in commands_run:
		os.system(i)
	os.chdir(f"{project_name}/src/{package_name}")
	initilizeJAVA(f"{filename}.java", package_name)
	os.chdir("../..")
	editJSON(f"{filename}.java")

createJavaProject("testproject", "testproject", "mainclass.java")
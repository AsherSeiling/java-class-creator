import sys
import os

# Initilizes the java file
def initilizeJAVA(filename, packageName):
	javafile = open(filename, "w+").read()
	java_code = [f"package {packageName};", f"public class {filename.split('.')[0]}" + "{", "	public static void main(String[] args){","	}" ,"}"]
	for i in java_code:
		javafile.write(f"{i}\n")

# Edit the JSON file
def editJSON(mainfilename):
	jsonfile = open("config.json", "w+").read()
	jsoncode = ["{", f"	\"mainfile\" : \"{mainfilename}\"",  "}"]
	for i in jsoncode:
		jsonfile.write(f"{i}\n")

# The main function to create a new java project
def createJavaProject(project_name, package_name, main_file_name):
	filename = main_file_name.split('.')[0]
	commands_run = [f"mkdir {project_name}", f"cd {project_name}", "mdkir bin src", "cd src", f"mkdir {package_name}", f"cd {package_name}", f"touch {filename}.java", "cd ../../bin", f"mkdir {package_name}", f"cd {package_name}", "cd ../..", "touch config.json", f"cd src/{package_name}"]
	for i in commands_run:
		os.system(i)
	initilizeJAVA(f"{filename}.java", package_name)
	os.system("cd ../..")
	editJSON(f"{filename}.java")
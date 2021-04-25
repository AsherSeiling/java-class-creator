import os
import sys
import time

# Build the Java files
def buildFiles():
	os.chdir("src/")
	os.chdir(os.listdir()[0])
	files = os.listdir()
	compableFiles = []
	for i in files:
		if i.split(".")[1].lower() == "java":
			compableFiles.append(i)
	for i in compableFiles:
		os.system(f"javac {i}")

# Move the class files
def moveClassFiles():
	os.chdir("../..")
	classfiles = []
	# Find the class files
	filesdir = os.listdir("src")[0]
	possibleJavafiles = os.listdir(f"src/{filesdir}")
	for i in possibleJavafiles:
		buffer = i.split(".")
		if buffer[1] == "class":
			classfiles.append(i)
	# Append the files
	for i in classfiles:
		filesdir = os.listdir("src")[0]
		filesbin = os.listdir("bin")[0]
		os.system(f"mv src/{filesdir}/{i} bin/{filesbin}/{i}")

# Main function
def buildProject():
	rows, columns = os.popen('stty size', 'r').read().split()
	buffer = ""
	for i in range(int(columns)):
		buffer += "-"
	time1 = time.time()
	buildFiles()
	time2 = time.time()
	moveClassFiles()
	print(buffer)
	print(f" Build Complete\n Buildtime: {time2 - time1} seconds")

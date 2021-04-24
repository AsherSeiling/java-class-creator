import os
import time

def compile_and_run(name):
	rows, columns = os.popen('stty size', 'r').read().split()
	buffer = ""
	for i in range(int(columns)):
		buffer += "-"
	print(f"Starting Compilation and run process\n{buffer}")
	time1 = time.time()
	os.system(f"javac {name}")
	time2 = time.time()
	os.system(f"java {name}")
	print(buffer)
	print(f" jvclass: Process complete\n Compilation time: {time2 - time1} seconds")

def compRun(name):
	namesplit = name.split(".")
	if namesplit[1] == "java":
		compile_and_run(name)
	else:
		print(f" Error: filetype \".{namesplit[1]}\" should be \".java\"")

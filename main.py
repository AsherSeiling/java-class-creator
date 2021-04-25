import os
import sys
# Import modules for the command functions
import commands.newClass as ncs
import commands.newMainClass as nmcs
import commands.compRun as comprn
import commands.createJavaProject as cjpj


programName = "jvclass"
# Commands list
commands_doc = [f"Here is the documentation for {programName}", f" {programName} new-main-class <class name>", f" {programName} new-class <class name>", f" {programName} comp-run <filename>", f" {programName} new-project <project name> <package name> <main file name>"]

# Initilization for reading of the command to see if the user needs help or if there are too many args
try:
	enable_run = True
	if sys.argv[1].lower() == "-h":
		enable_run = False
		for i in commands_doc:
			print(i)
	if len(sys.argv) == 1:
		enable_run = False
except:
	enable_run = False
	print(f"Error: type \"{programName} -h\" for help with the program")

# Main Function
def main():
	command = sys.argv
	if command[1].lower() == "new-main-class":
		nmcs.new_main_class(command)
	elif command[1].lower() == "new-class":
		ncs.new_class(command)
	elif command[1].lower() == "comp-run":
		comprn.compRun(command[2])
	elif command[1].lower() == "new-project":
		cjpj.createJavaProject(command[2], command[3], command[4])
	else:
		print(f" Error: Command Argument \"{command[1]}\" not found try \"-h\" for help with commands")


# Run the code if it is enabled
if enable_run == True:
	main()

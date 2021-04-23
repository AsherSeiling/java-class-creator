import os
import sys
import newClass as ncs
import newMainClass as nmcs


programName = "jvclass"
# Commands list
commands_doc = [f"Here is the documentation for {programName}", f" {programName} new-main-class <class name>", "   Creates a new class file with \"Public static void main(String[] args){}\"", f" {programName} new-class <class name>"]

# Initilization for reading of the command to see if the user needs help or if there are too many args
enable_run = True
if len(sys.argv) > 3:
	enable_run = False
	print("Command has only two additional argument\nAdditional args " + str(len(sys.argv) - 1))
if sys.argv[1].lower() == "-h":
	enable_run = False
	for i in commands_doc:
		print(i)

# Main Function
def main():
	command = sys.argv
	if command[1].lower() == "new-main-class":
		nmcs.new_main_class(command)
	elif command[1].lower() == "new-class":
		ncs.new_class(command)
	else:
		print(f" Error: Command Argument \"{command[1]}\" not found try \"-h\" for help with commands")


# Run the code if it is enabled
if enable_run == True:
	main()
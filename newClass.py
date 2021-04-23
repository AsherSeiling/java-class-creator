import os
import sys

def new_class(args):
	name = str(args[2])
	codetamplate = [f"public class {name}" + "{", "}"]
	os.system(f"touch {args[2]}.java")
	files = open(f"{args[2]}.java", "w+")
	for i in codetamplate:
		files.write(f"{i}\n")

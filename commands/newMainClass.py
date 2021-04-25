import os
import sys

def new_main_class(args):
	name = str(args[2].split(".")[1])
	codetamplate = [f"public class {name}" + "{", "	public static void main(String[] args){","	}" ,"}"]
	os.system(f"touch {args[2]}.java")
	files = open(f"{args[2]}.java", "w+")
	for i in codetamplate:
		files.write(f"{i}\n")
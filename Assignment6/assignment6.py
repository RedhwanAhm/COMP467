# Redhwan Ahmed
# Assignment 6
# Professor Chaja - COMP 467

import argparse

# 1.) Create the argument parser
parser = argparse.ArgumentParser(description="Import a text file and optionally print each line.");
# 2.) Add an argument for filepath
parser.add_argument("filepath", help="the path to the text file");
# 3.) Add the verbose argument with the action to store true if used in the command line.
parser.add_argument("-v", "--verbose", action="store_true", help="print each line");
# 4.) Set up the parser for args to be passed in through the command line.
args = parser.parse_args();

# 5.) Import the file, and read the lines.
input_file = open(args.filepath, "r");
lines = input_file.readlines();

# 6.) If the verbose statement is given, then print the lines to the screen.
if(args.verbose):
    print("Lines in the text file: ")
    for line in lines:
        print(line);

# 7.) Get the length of the file
line_count = len(lines);
print("Line count: "+str(line_count))


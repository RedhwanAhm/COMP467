# Redhwan Ahmed
# Assignment 8
# Professor Chaja - COMP 467

import subprocess
import shlex

# Set the command and arguments
command = 'dir "C:/Users/Redhwan Ahmed/Desktop/random/random" /s /b /o-s'

# Use shlex.split to split the command into a list of arguments
args = shlex.split(command)

# Use subprocess.Popen to execute the command
process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Read the output of the command one line at a time
largest_file = ""
largest_size = 0
for line in iter(process.stdout.readline, b''):
    # Parse the line to get the file name and size
    parts = line.decode().strip().split("\\")
    filename = parts[-1]
    try:
        size = int(parts[-2])
        if size > largest_size:
            largest_file = filename
            largest_size = size
    except ValueError:
        # Ignore any lines that don't have a file size
        pass

# Print the largest file and its size
if largest_file:
    print("Largest file:", largest_file)
    print("Size:", largest_size, "bytes")
else:
    print("No files found.")
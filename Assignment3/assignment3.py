# Redhwan Ahmed
# Assignment 3
# Professor Chaja - COMP 467

import os
import time

checked_files = set();

while True:
    # Get a list of all files in the folder.
    files = os.listdir("./");
    
    # Check if any new files have been added since the last iteration.
    for file in files:
        file_path = os.path.join("./", file);

        # Check if the file in the path is a file and also if it hasn't been checked before.
        if os.path.isfile(file_path) and file not in checked_files:

            # Add the checked file to the checked_files set.
            checked_files.add(file);
            file_created = time.ctime(os.path.getctime(file_path));

            # Print all the necessary information.
            print("New file found: " + file);
            print("File type: " + os.path.splitext(file)[1]);
            print("File created: " + file_created);
    
    # Wait for 1 second before checking again.
    time.sleep(1)
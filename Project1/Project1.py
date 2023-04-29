# Redhwan Ahmed
# Project 1
# Professor Chaja - COMP 467

import os
import csv

# This function removes '/' from the inputs given
def slash_remover(list):
    result_list = []
    for i in range(0, len(list)):
        result_list.append(list[i].split("/"))
        if '' in result_list[i]:
            result_list[i].remove("");
    return result_list;

# This function removes backslashes in a list, where they show up as elements.
def list_backslash_n_remover(list):
    result_list = [];
    for i in range(0, len(list)):
        result_list.append(list[i].replace("\n", ""))
    return result_list

# This function removes the '\n' from the lines passed to it.
def backslash_n_remover(line):
    result = line.replace("\n", "")
    result = result.strip();
    result = result.split();
    return result

# Step 1: Import the two text files to be parsed. Using validation as well.
input1 = "Xytech.txt"
input2 = "Baselight_export.txt"

# Check if Xytech.txt exists.
if not os.path.isfile(input1):
    print(f"{input1} does not exist")
    exit()

# Check if 
if not os.path.isfile(input2):
    print(f"{input2} does not exist")
    exit()

with open(input1, "r") as input1:
    xytech = input1.readlines()

with open(input2, "r") as input2:
    baselight_export = input2.readlines()

# Close the above input files.
input1.close() 
input2.close()

# Step 2: Process the xytech and baselight_export line arrays and make them CSV "friendly"
# Remove empty lines
while "\n" in xytech:
    xytech.remove("\n");
while "\n" in baselight_export:
    baselight_export.remove("\n");

# Remove excess "\n" from Xytech ingest
xytech = list_backslash_n_remover(xytech);

# Separate Xytech into separate arrays
location_index = xytech.index("Location:");
notes_index = xytech.index("Notes:");

# Xytech User Details Subset
xytech_user_details = xytech[0:location_index]
xytech_user_details.append(xytech[notes_index+1])
# Process for inserting into the CSV File
for i in range(0, len(xytech_user_details)):
    xytech_user_details[i] = xytech_user_details[i].strip()
    if ":" in xytech_user_details[i]:
        xytech_user_details[i] = xytech_user_details[i].split(":")[1].strip()

# Xytech Locations Subset
xytech_locations = slash_remover(xytech[location_index+1:notes_index]);

# Process for to make comparisons to baselight_export

# Baselight_export into separate Arrays
baselight_export_locations = []
baselight_export_frames = []
# Process such that the filepath and frame numbers are split up into their own separate arrays.
for i in range(0, len(baselight_export)):
    temp_list = baselight_export[i].split(" ", 1)
    baselight_export_locations.append(temp_list[0])
    baselight_export_frames.append(temp_list[1])

# This processes the locations in the baselight_export
baselight_export_locations = slash_remover(baselight_export_locations);

# Process the baselight_export frames.


# Step 3: Now we will compare the locations provided in Xytech and Baselight Export and create a new location array that has them ready for the CSV file. The reason for doing this is because baselight_export_locations has the frame numbers in ascending order with each location too, whereas xytech only has the list of locations. Thus we will replace each of the locations in baselight_export_locations with whats given to us in xytech locations.
    # ex:
    # xytech has:               /hpsans13/production/starwars/reel1/partA/1920x1080
    # baselight_export has:     /images1/starwars/reel1/partA/1920x1080
    # result will be:           /hpsans13/production/starwars/reel1/partA/1920x1080

# I'll approach this by removing three columns from the two dimensional array I've made for baselight_export_locations.
for i in range(0, len(baselight_export_locations)):
    temp_array = baselight_export_locations[i]
    baselight_export_locations[i] = temp_array[3:]

# After removing the three columns, each element in baselight_export_locations is unique and can be checked to see if it's a subset of the xytech locations array.
for i in range(0, len(baselight_export_locations)):
    for j in range(0, len(xytech_locations)):
        subset = all(element1 in xytech_locations[j] for element1 in baselight_export_locations[i]);
        if subset:
            baselight_export_locations[i] = xytech_locations[j];  

# Step 4: create a modified baselight_export_frames file that holds the numbers in ranges rather than all of them listed.

# Created a new baselight_export_frames array to hold the processed frames.
bef_new = [];
# Start a for loop that will get every list in baselight_export_frames.
for list in baselight_export_frames:
    mod_bef = []; # temporary array
    i = 0
    # Using a while loop to work until i has reached the end of the list.
    while i < len(list):
        j = i
        # Using this while loop, we use the variable j to find the end point of a range.
        while j < len(list) - 1 and list[j+1] == list[j] + 1:
            j += 1
        # Only append the variables if j = i or if a range is found.
        if j == i:
            mod_bef.append(str(list[i]))
        else:
            mod_bef.append(str(list[i]) + "-" + str(list[j]))
        # Move i to the end of the range after we've appended the last range.
        i = j + 1
    # Append this list to the bef_new array
    bef_new.append(mod_bef)
# Set baselight_export_frames to bef_new
baselight_export_frames = bef_new;

output = [];
counter = 0;
for i, paths in enumerate(baselight_export_locations):
    for j, frame_ranges in enumerate(baselight_export_frames[i]):
        output.append(','.join(paths + [frame_ranges]))

for i in range(0, len(output)):
    output[i] = output[i].split(",")

# Step 5: Output to the CSV File.

# Create the CSV writer
csv_out = open("output.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csv_out)

# Write the user details into the row.
writer.writerow(xytech_user_details)
for i in range (0, 2):
    writer.writerow("")
for line in output:
    writer.writerow(line)
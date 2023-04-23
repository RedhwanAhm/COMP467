# Redhwan Ahmed
# Assignment 4
# Professor Chaja - COMP 467

# Read the contents of the input file.
with open('lesson4_folderexample.txt', 'r') as file_paths:
    contents = file_paths.readlines()

# Initialize variables to keep track of fixed and unfixed paths.
fixed_paths = []
unfixed_paths = []

# Loop over each line in the input file.
for path in contents:
    # Remove any whitespace from the beginning and end of the path.
    path = path.strip()

    # Check if the path contains spaces
    if ' ' in path:
        # Replace spaces with underscores and append to fixed_paths list
        fixed_path = path.replace(' ', '_')
        fixed_paths.append(fixed_path)

        # Print a message indicating the path was fixed
        print("Fixed path: \n" + path + " -> \n" +fixed_path+"\n")
    else:
        # Append the path to the unfixed_paths list
        unfixed_paths.append(path)

# Print a summary of fixed and unfixed paths
print("Fixed paths: " + str(len(fixed_paths)))
for path in fixed_paths:
    print(path)
    
print("Unfixed paths: " + str(len(unfixed_paths)))
for path in unfixed_paths:
    print(path)
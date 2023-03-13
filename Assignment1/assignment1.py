# Redhwan Ahmed
# Assignment 1
# Professor Chaja - COMP 467

import random;
import os;

# Step 1: Check for input file. If it doesn't exist generate random number list of length 20.
path = "./input.txt";
outPath = "./output.txt";
if (not os.path.isfile(path)):
    inputFile = open("input.txt", "w");
    for i in range(0, 20):
        inputFile.write(str(random.randint(1,1000))+" ");
    inputFile.close();

# Step 2: Read random number list and place into an array.
infile = open("input.txt", "r");
stringOfNums = infile.readline().split(" ");
intNums = [];
for i in range(0, len(stringOfNums)):
    if (stringOfNums[i].isdigit()):
        intNums.append(int(stringOfNums[i]));
infile.close();

# Step 3: Sort the Array from greatest to least.
intNums.sort(reverse=True);

# Step 4: Write output to the console and output file. Only will run if the output file doesnt exist
outputFile = open("output.txt", "w");
print("Unsorted List:", end=" ");
outputFile.write("Unsorted List: ");
for i in range(0, len(stringOfNums)):
    print(stringOfNums[i], end=" ");
    outputFile.write(stringOfNums[i]+" ");
print();
outputFile.write("\n");
print("Sorted List:",end=" ");
outputFile.write("Sorted List: ");
for i in range(0, len(intNums)):
    print(intNums[i],end=" ");
    outputFile.write(str(intNums[i])+" ");
print();
outputFile.write("\n");
print("Largest number: "+str(intNums[0]));
outputFile.write("Largest number: "+str(intNums[0]));
outputFile.close();
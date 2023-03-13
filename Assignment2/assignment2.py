# Redhwan Ahmed
# Assignment 2
# Professor Chaja - COMP 467
input_file = open("ingest_this.txt", "r");
input_lines = input_file.readlines();
input_string = [];
vowels = "AEIOUaeiou"
for line in input_lines:
    for vowel in vowels:
        line = line.replace(vowel, "9");
    print(line);



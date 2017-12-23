# A program to read information from file
# Author: Ariful Islam

# Open a file
fo = open("example.txt", "r+")
str = fo.read(50);
print("Read String is : ", str)
# Close opened file
fo.close()
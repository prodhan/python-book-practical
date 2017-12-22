# A program to  calculate the average of a set of N numbers
# Author: Ariful Islam

n = int(input("How many numbers you have? "))
a = []
for i in range(0, n):
    item = int(input("Enter integer number: "))
    a.append(item)
avg = sum(a)/n
print("Average of entered numbers is: ", avg)

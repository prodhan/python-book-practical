# A program to compare three numbers
# Author: Ariful Islam

num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: "))
num3 = int(input("Input number 3: "))

if num1 > num2 and num1 > num3:
    print("Largest number is: ", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is: ", num2)
else:
    print("Largest number is: ", num3)


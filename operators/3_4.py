# A program to compare two integer numbers using logical operator
# Author: Ariful Islam

num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: "))

greater = num1 if num1 > num2 else num2

print("Greatest value is ", greater)


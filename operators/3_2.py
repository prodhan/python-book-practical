# A program to calculate the area of a triangle
# Author: Ariful Islam
from math import sqrt

a = int(input("Enter the arm of a triangle "))
b = int(input("Enter the arm of a triangle "))
c = int(input("Enter the arm of a triangle "))

s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of the triangle is", area)

# A program to calculate the area of triangle using function
# Author: Ariful Islam

from math import sqrt
def CalculateArea():
    a = int(input("Enter the arm of a triangle "))
    b = int(input("Enter the arm of a triangle "))
    c = int(input("Enter the arm of a triangle "))
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

print("The area of the triangle is", CalculateArea())
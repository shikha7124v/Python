# Create a program to calculate the area and circumference of the circle. ask user radius

radius = input("Enter the radius : ")
import math
pi = round(math.pi, 2)
area = pi * float(radius) * float(radius)
print(area)

circumference = 2.00 * pi * float(radius)
print(circumference)


"""
Assignment 1
"""
# Question 1
name = input("What is your name? ")
print("Pleased to meet you,", name, "!")

yr1 = int(input("How many courses did you take in first year? "))
yr2 = int(input("How many courses did you take in second year? "))
yr3 = int(input("How many courses did you take in third year? "))

no_courses = (40 - yr1 - yr2 - yr3)
print("Great! You have", no_courses, "courses left to take, good luck!")

# Question 2
courses = """ 
1. CISC 101
2. CISC 102
3. CISC 121
4. CISC 124
5. CISC 181"""

print(courses)
int(input("Which course would you like to add to your calendar? "))

# Question 3
import math

x1 = int(input("Please enter the first x coordinate: "))
y1 = int(input("Please enter the first y coordinate: "))

x2 = int(input("Please enter the second x coordinate: "))
y2 = int(input("Please enter the second y coordinate: "))

dist = math.sqrt(abs((x2 - x1)^2 + (y2 - y1)^2))
rounded_dist = round(dist, 3)
midpoint = ((x1 + x2)/2, (y1 + y2/2))

print("The distance is", rounded_dist, "and the midpoint is", midpoint)
"""
Assignment 2
"""

# Question 1: Adding courses to a calendar from a menu
courses = """ 
1. CISC 101
2. CISC 102
3. CISC 121
4. CISC 124
5. CISC 181"""

print(courses)
course_selection = int(input("Which course would you like to add to your calendar? "))

if course_selection == 1:
    print("You have added CISC 101")
elif course_selection == 2:
    print("You have added CISC 102")
elif course_selection == 3:
    print("You have added CISC 121")
elif course_selection == 4:
    print("You have added CISC 124")
elif course_selection == 5:
    print("You have added CISC 181")
else:
    print("This option is invalid, select a course from the menu!")
    
# Question 2: Creating a restaurant selector
restaurants = ("Kpop Sub Sushi", "Score Pizza", "Amadeus Cafe", "Casa Domenico", "Kingston Brew Pub")

vegetarian = input("Is anyone in your party vegetarian? ")
vegan = input("Is anyone in your party vegan? ")
gluten = input("Is anyone in your party gluten-free? ")

if vegetarian == "yes":
    if vegan == "yes":
        print("Your options are:", restaurants[2], restaurants[4], sep ="\n")
    else:
        if gluten == "yes":
            print("Your options are:", restaurants[1], restaurants[2], restaurants[4], sep ="\n")
        else:
            print("Your options are:")
            print(*restaurants[1:], sep ="\n")
else:
    if vegan == "yes":
        print("Your options are:", restaurants[2], restaurants[4], sep ="\n")
    else:
        if gluten == "yes":
            print("Your options are:", restaurants[1], restaurants[2], restaurants[4], sep ="\n")
        else:
            print("Your options are:")
            print(*restaurants, sep ="\n")

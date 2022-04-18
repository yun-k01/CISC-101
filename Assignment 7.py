"""
Assignment 7: Student Marks Directory
"""
import random


def generateData(nosStudents):
    """
    This program generates a dictionary of student numbers, and three student marks for each student, 
        given the number of students.
    Parameters:
        nosStudents - integer
    Return:
        stuData - dictionary of student numbers (integer) and student grades (integer)
    """
    # creating a empty dictionary to store the student numbers and associated grades
    stuData = {}
    grades = {}
    
    for i in range(nosStudents):
        
        # defining the range that the student number can belong to, 1000-9000 inclusive
        stuNumber = random.randint(1000, 9000)

        for j in range(1):
            # defining the range that grades can belong to, 0-100 inclusive
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            z = random.randint(0, 100)
            
            # assigning a grade to each assignment
            grades = {"A1": x, "A2": y, "A3": z}
        
        # assigning the grades to a student number
        stuData[stuNumber] = grades
        
    return stuData
    


def averageMark(stuNumber, stuData):
    """
    This function calculates the average grade of a given student
    Parameters:
        stuNumber - integer
        stuData - dictionary of student numbers (integer) and student grades (integer)
    Return:
        avgGrade - float
    """
    # if the student number exists, it will calculate the mean of the three assignments
    if stuNumber in stuData:
        avgGrade = (stuData[stuNumber]["A1"] + stuData[stuNumber]["A2"] + stuData[stuNumber]["A3"]) / 3
    
    # if the student number doesn't exist, the average is equal to 0
    else:
        avgGrade = 0
    
    return avgGrade 

   
   
def lowestMark(stuData):
    """
    This function finds the lowest grade associated with an assignment for each student number
    Parameters:
        stuData - dictionary of student numbers (integer) and student grades (integer)
    Return:
        lowMarks - list of tupples of student numbers (integer) and their worst assignment (string)
    """
    lowMarks = []
    
    # finding the lowest grade of all the assignments for each student
    for key in stuData:
        lowest = min(stuData[key]["A1"], stuData[key]["A2"], stuData[key]["A3"])
        
        for asg in stuData[key]:
            
            # finding the assignment name that corresponds to the lowest grade
            if stuData[key]["A1"] == lowest:
                asg = "A1"
            elif stuData[key]["A2"] == lowest:
                asg = "A2"
            else:
                asg = "A3"

        
        # changing the tupple to contain the student number and the worst assignment
        lowMarks.append([key, asg])
    
    return format(lowMarks)
    

    
def main():
    
    # getting the number of students
    nosStudents = int(input("How many students do you have? "))

    # print the results and the dictionary of student numbers and grades
    print("There are", nosStudents, "students.")
    
    # creating the student dictionary given nosStudents
    stuData = generateData(nosStudents)
    
    # print the student dictionary
    print("Here are their student numbers and grades:", stuData, sep = "\n")
    
    # ask which student they want to see the average mark for & print the results.
    stuNumber = int(input("Which student's average mark would you like to see? "))
    avgMark = averageMark(stuNumber, stuData)
    print(stuNumber, "has an average of", avgMark)
    
    # show the list of students and the assignment on which they got the lowest mark.
    lowMark = lowestMark(stuData)
    print("\n", "The students got the lowest marks in these assignments [student number, assignment]: ", "\n", lowMark, sep = "")

    # indicating end of program
    print("\n", "Thanks for using directory for student marks!", sep = "")


main()

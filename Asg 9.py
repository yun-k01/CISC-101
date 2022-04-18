"""
Yun Kyaw, 20177325
Assignment 9: User ID and Password Generator
March 25, 2022
"""
import urllib.request

import random

import string


def readWebPage(url1, url2):
    """
    This function reads two urls and returns the words as lists
    Parameters:  
        url1 - string of a url to be read
        url2 - string of a url to be read
    Returns: 
        listOfWords1 - list of strings
        listOfWords2 - list of strings
    """
    try:
        #make a connection
        response1 = urllib.request.urlopen(url1)
        response2 = urllib.request.urlopen(url2)        

        #read the data into a single string
        data1 = response1.read().decode('utf-8')
        data2 = response2.read().decode('utf-8')

        #create a list of words from the string
        listOfWords1 = data1.split()
        listOfWords2 = data2.split() 
        
    except:
        print("There was an error with one of the URLs!")
        return []
    
    return listOfWords1, listOfWords2



def userIDGenerator(listOfWords1, listOfWords2):
    """
    This function generates a username
    Parameters: 
        listOfWords1 - list of strings
        listOfWords2 - list of strings
    Return:
        Username - string
    """
    # choosing a random word from each list
    word1 = random.choice(listOfWords1)
    word2 = random.choice(listOfWords2)
    
    # capitalizing the selected words
    word1 = word1.capitalize()
    word2 = word2.capitalize()
    
    # creating a single string consisting of both words 
    Username = word1+word2
    
    return Username

    

def passwordGenerator():
    """
    This function generates a password
    Parameters:
        none
    Return:
        Password - string
    """
    # determining the length of the password (8-10 inclusive)
    length = random.randint(8, 12)
    letters = 0
    Password = ""
    
    while letters != length:
        
        # generating the capital letter
        if letters != length:
            upperCase = random.choice(string.ascii_uppercase)
            Password = Password+upperCase
            letters += 1
        
        # generating lowercase letters
        if letters != length:
            for i in range(2):
                lowerCase = random.choice(string.ascii_lowercase)
                Password = Password+lowerCase
                letters += 1
        
        # generating a number larger than 5
        if letters != length:
            no2 = random.choice(string.digits[6:])
            Password = Password+no2
            letters += 1
        
        # generating a number less than or equal to 5
        if letters != length:
            no1 = random.choice(string.digits[:6])
            Password = Password+no1
            letters += 1
        
        # generating punction
        if letters != length:
            punct = random.choice(string.punctuation)
            Password= Password+punct
            letters += 1
            
    return Password



def loopFunction(looping):
    """
    This function will loop to create new User IDs and Passwords until the user is content
    Parameters:
        looping - string
    Return:
        none
    """
    # reading files with lists for User ID and Password
    adjectives, animals = readWebPage("https://tinyurl.com/ywy6f72e", "https://research.cs.queensu.ca/home/cords2/animals.txt")
    
    choice = 0
    while choice != 1:
        
        # continuing loop if user wants new User ID/Password
        if looping == "Yes":
            Username = userIDGenerator(adjectives, animals)
            print("USERID:", Username)
            Password = passwordGenerator()
            print("PASSWORD:", Password)
            looping = input("Would you like another User ID/Password? (Yes/No) ")
        
        # ending loop if user wants new User ID/Password
        elif looping == "No":
            choice = 1
        
        # continuing loop if user has not entered Yes or No
        else: 
            print("Input is invalid.")
            looping = input("Would you like another User ID/Password? (Yes/No) ")
            
    return



def main():
    # reading files with lists for User ID and Password
    adjectives, animals = readWebPage("https://tinyurl.com/ywy6f72e", "https://research.cs.queensu.ca/home/cords2/animals.txt")
    
    # telling the user what is happening
    print("Hi! I will generate a User ID and secure Password for you...")
    
    # telling the user their User ID
    Username = userIDGenerator(adjectives, animals)
    print("USERID:", Username)
    
    # telling the user their Password
    Password = passwordGenerator()
    print("PASSWORD:", Password)
    
    # generates new User ID/Password if the user would like
    looping = input("Would you like another User ID/Password? (Yes/No) ")
    loopFunction(looping)
    
    # indicating the end of the program
    print("Be sure not to share your User ID and Password... Good luck, have fun!")
    
main()
    
    
    
    
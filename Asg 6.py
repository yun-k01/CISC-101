'''
Yun Kyaw, 20177325
Asg 6: Wordle 101
'''
import random

def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the secret word
    """
    
    validWords = ["could", "smile", "ultra", "extra", \
                  "beacon", "hearts", "cap", "wordle", \
                  "computing", "program", "python"]

    #random.randint(0, 5) will generate an integer between 0 and 5 (inclusive)
    #this is then used to select a value from the list validWords.

    wordPosition = random.randint(0,5)

    return validWords[wordPosition]


def checkLetters(secretWord, userWord):
    """
    This function checks the letters guessed by the user against the secret
    word and informs the user as to which letters are in the correct location,
    which letters are in the word but not in the correct location and which
    letters are not in the word.
    Parameters:   secretWord, userWord - strings
    Returns:  None
    """
    # for loop to check userWord letters with secretWord letters, limited by the length of secretWord
    for i in range(min(len(userWord), len(secretWord))):
        
        # telling the player if their letters are correct
        if userWord[i] == secretWord[i]:
            print(userWord[i], "- correct place")
        elif userWord[i] in secretWord:
            print(userWord[i], " - incorrect place")
        else:
            print(userWord[i], "- not in word")

    
def checkForDuplicates(userWord):
    """
    This function checks the user's word for duplicate letters.
    If there are duplicate letters, the function returns True, otherwise, False.
    Parameters:  userWord - string
    Return:  Boolean
    """
    for letter in userWord:
        # checking if there are >1 of a letter in a word
        if userWord.count(letter) > 1:
            return True

    
def play(secretWord):
    """
    This function allows the user to play the game, entering up to 6 words to
    try to guess the secret word. When the correct word is guessed, the play
    stops and the user is congratulated.
    Parameters: string representing the secretWord
    Return Value:  None
    """

    for x in range(6):
        
        userWord = input("Guess a word: ")
        # to be used to count the score if the user doesnt guess correctly
        score = 0
        
        # ensure userWord is a word without duplicates
        while not userWord.isalpha() or checkForDuplicates(userWord) == True:
            userWord = input("Incorrect input, please enter a word without duplicated letters: ")
            
        # checking if userWord has guessed correctly
        if userWord == secretWord:
            print("Congratulations! ", secretWord.capitalize(), " was the secret word!", sep = "")
            score = 1
            break
        else:
            checkLetters(secretWord, userWord)
            score = 0
            continue
        
    # tells user what the word was if they didnt get it
    if score == 0:
        print("Better luck next time! The secret word was", secretWord)
        

def main():
    """
    This implements the user interface for the program.
    """
    # selecting the secret word
    secretWord = chooseWord()
    print(secretWord)
    
    # intro to the game
    print("Hi! Welcome to Wordle")
    
    # starting the game
    play(secretWord)
    
    # printing goodbye
    print("Thanks for playing!")


main()
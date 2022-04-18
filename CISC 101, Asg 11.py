"""
Yun Kyaw, 20177325
Assignment 11: Card Game
April 8, 2022
"""
import random

def cardFromDeck(deck):
    """
    this function selects a random card to be flipped and removes it from the deck
    input:
        deck - list of strings
    return:
        card - string
    """
    card = random.choice(deck)  # selecting a random card from the deck
    deck.remove(card)  # removing the selected card from the deck
    
    return card



def dealHand(deck):
    """
    this function selects 5 cards from a deck to into a list and removes the cards from the deck
    input:
        deck - list of strings
    return:
        hand - list of strings
        
    """
    hand = []  # storing the selected cards into a list
    
    for i in range(5):
        card = random.choice(deck)  # selecting a random card
        hand.append(card)  # adding the card to a list
        deck.remove(card)  # removing the card from the deck
        
    return hand
    
    

def userTurn(deck, userHand, userChoice, dealCard):
    """
    this function will change the hand of the player or will flip a card depending on their choice
    input:
        deck - list of strings
        userHand - list of strings
        userChoice - string
        dealCard - string
    return:
        userCards - list of strings
        """
    # if the user selects to choose a card from the deck, the selected card will be added to their hand and they will remove a card in their hand
    if userChoice == "D":
        print("Your hand:", userHand)
        userHand.append(dealCard)  # adding the card to the user's hand
        removeCard = input("Which card would you like to remove? " )
        
        # ensuring the selected card is valid card
        while not removeCard in userHand:
            removeCard = input("Invalid input. Which card would you like to remove? ")

        # removing the selected card and telling the user their new hand of cards   
        if removeCard in userHand:
            userHand.remove(removeCard)
            print("Your hand:", userHand)
    
    # if the user selects F, the computer will flip a card during it's turn

    return userHand
    


def computerTurn(deck, compHand, userChoice):
    """
    this function gives the computer 5 cards and removes them from the deck
    input:
        cards - list of strings
    return:
        compCards - list of strings
    """
    # if the user selected F, the computer will keep the flipped card and remove a card in their hand
    if userChoice == "F":
        dealCard = cardFromDeck(deck)
        compHand.append(dealCard)
        print("The flipped card is:", dealCard)
        removeCard = random.choice(compHand)
        compHand.remove(removeCard)
        print("Computer hand:", compHand)
            
    # if the user selected D, the computer will flip a card
    else:
        flipCard = cardFromDeck(deck)
        print("Computer hand:", compHand)
    
    return compHand



def checkWin(compCards, userCards):
    """
    this function checks which hand of cards wins
    input:
        compCards - list of strings
        userCards - list of strings
    return:
        winner - string
    """
    # checking sum of user
    valuesUser = []  # list to store the rank of the cards
    userSum = 0
    for i in range(5):
        valuesUser.append(userCards[i][0])  # storing the rank of each card

    for i in range(5):
        if valuesUser[i].isalpha() == True:
            userSum += 10  # if the card is A, K, Q, or J, it has a value of 10
        else: 
            userSum += int(valuesUser[i])  # making the card an integer so it can be added to the sum
    
    # checking sum of computer
    valuesComp = []  # list to store the rank of the cards
    compSum = 0
    for i in range(5):
        valuesComp.append(userCards[i][0])  # storing the rank of each card

    for i in range(5):
        if valuesComp[i].isalpha() == True:
            compSum += 10  # if the card is A, K, Q, or J, it has a value of 10
        else: 
            compSum += int(valuesComp[i])  # making the card an integer so it can be added to the sum
    
    # comparing sums
    winningVal = max(userSum, compSum)

    if winningVal == userSum:
        winner = "User"
    elif winningVal == compSum:
        winner = "Computer"
    elif userSum == compSum:
        winner= "Tie"
    else:
        winner = "None"

    # checking suits of user
    for i in range(5):
        if userCards[i] in userCards[i-1]:
            winner = userCards
        
    # checking suits of computer
    for i in range(5):
        if compCards[i] in compCards[i-1]:
            winner = compCards
        
    return winner


def main():
    cards = ["AH", "AD", "AS", "AC", "KH", "KD", "KS", "KC",
                    "QH", "QD", "QS", "QC", "JH", "JD", "JS", "JC",
                    "10H", "10D", "10S", "10C", "9H", "9D", "9S", "9C",
                    "8H", "8D", "8S", "8C", "7H", "7D", "7S", "7C",
                    "6H", "6D", "6S", "6C", "5H", "5D", "5S", "5C",
                    "4H", "4D", "4S", "4C", "3H", "3D", "3S", "3C",
                    "2H", "2D", "2S", "2C"]
    # starting the game by giving the user their hand and the computer it's hand
    userHand = dealHand(cards)
    print("Your hand:", userHand)
    compHand = dealHand(cards)
    print("Computer hand:", compHand)
        
    # loop control so game is played again if there is no winner
    loopControl = 0
    while loopControl != 1:

        # user's turn
        print("\n")
        dealCard = cardFromDeck(cards)
        print("The flipped card is:", dealCard)  # flipping a card to start the game
        userChoice = input("What would you like to do? D = choose from deck, F = pick up flipped card: ")
                
        # making sure the user input is valid
        while userChoice != "D" and userChoice != "F":
            userChoice = input("Invalid Input. What would you like to do? D = choose from deck, F = pick up flipped card: ")
                
        userHand = userTurn(cards, userHand, userChoice, dealCard)
                
        # computer's turn
        compHand = computerTurn(cards, compHand, userChoice)
            
        # checking the winner
        winner = checkWin(compHand, userHand)
            
        # informing the winner and playing again if there is no winner
        print("\n")
        if winner == "User":
            print("Congratulations! You are the winner!")
            loopControl = 1
        elif winner == "Computer":
            print("Sorry! The computer won!")
            loopControl = 1
        elif winner == "Tie":
            print("There was a tie!")
            loopControl = 1
        else:
            print("There is no winner! Play again!")    
    
    print("Thank you for playing!")

main()
"""
Assignment 3
"""

# Question 1: Creating Ascii Art

line = """_"""
straight = """| """
slash = """ \ """

for i in range(3):
    print(line * 18 + "\t" *2 + line*18)
    for i in range(2):
        print(straight + "\t" *4 + slash + "\t"*2 + slash + "\t"*4 + straight)
    print(straight + line * 15 + slash + "\t"*2 + slash + line * 14 + straight)
    for l in range(10):
        print(straight + "\t" + straight + "\t"*8 + straight + "\t" + straight)
    print("\t" + "~~~ oh no, our table, it's broken ~~~")
    
    
# Question 2: Wordle

# while loop for play again prompt
game = 0
while game != 1:

# player 1 prompt
    word = input("Player 1: Please enter a 5 letter word: ")
    word_count = 0
    while word_count != 1:
        if word.isalpha() == False:
            print("Incorrect input")
            word = input("Player 1: Please enter a 5 letter word: ")
        elif len(word) !=5 :
            print("Incorrect length")
            word = input("Player 1: Please enter a 5 letter word: ")
        else:
            word_count = 1

# player 2 prompt and score count
    print("\n", "Player 2 - it is your turn to guess letters", sep = '')
    let_count = 0
    score_count = 0
    letter = input("Please enter a letter: ")
    while let_count < 4:
        if letter.isalpha() == True and len(letter) == 1:
            letter = input("Please enter a letter: ")
            let_count += 1
            if letter in word:
                score_count += 1
        else:
            letter = input("Incorrect input, please enter a letter: ")
            if letter in word:
                score_count += 1

# print score
    print("You got a score of ", score_count, "/5", sep = '')

# play again prompt
    play = input("Would you like to play again? (yes/no) ")
    if play == "no" or play == "No":
        print("Thanks for playing")
        game = 1
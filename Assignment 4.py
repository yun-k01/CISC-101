"""
Assignment 4
"""
# Question 1: Writing functions to create Ascii art three times
# defining the main function, with nos indicating how many loops will be done
def main(nos):
    for i in range(nos):
        drawing()

# defining the function that will create the drawing
def drawing():
    
    # creating local constants
    line = """_"""
    straight = """| """
    slash = """ \ """

    # writing the code that will draw
    print(line * 18 + "\t" *2 + line*18)
    for i in range(2):
        print(straight + "\t" *4 + slash + "\t"*2 + slash + "\t"*4 + straight)
        print(straight + line * 15 + slash + "\t"*2 + slash + line * 14 + straight)
    for l in range(10):
        print(straight + "\t" + straight + "\t"*8 + straight + "\t" + straight)
    print("\t" + "~~~ oh no, our table, it's broken ~~~")
        
# executing the function 3 times
main(3)


# Question 2: Writing functions to create a banking simulator
# writing the main function to calculate banking
def main():
    # greet the user
    print("Hi, user!")
    
    # print menu options
    menuOptions()

    # get bank account balance
    accountBalance = getInitialBalance()
    print("You have $", accountBalance, " in your savings account!", sep = "")

    # get user's choice    
    optionNos = int(input("What would you like to do? "))
    
    # loopControl variable to control loop
    loopControl = 0
    while loopControl != 1:
        
        # perform the different options
        if optionNos == 1:
            accountBalance = withdrawl(accountBalance)
            print("You now have $", accountBalance, " in your savings account!", sep = "")
            optionNos = int(input("What would you like to do next? "))
        elif optionNos == 2:
            accountBalance = deposit(accountBalance)
            print("You now have $", accountBalance, " in your savings account!", sep = "")
            optionNos = int(input("What would you like to do next? "))
        elif optionNos == 3:
            print("You have $", accountBalance, " in your savings account!", sep = "")
            optionNos = int(input("What would you like to do next? "))
        elif optionNos == 4:
            loopControl = 1
            print("Exiting... Bye!")
        else:
            print("Invalid option, please select again.")
            optionNos = int(input("What would you like to do? "))

def withdrawl(accountBalance):
    """
    This function calculates a new account balance given an amount to withdraw from the account.
    """
    amtToWithdraw = getWithdrawlAmount()
    newBalance = accountBalance - amtToWithdraw
    return(newBalance)
    
def deposit(accountBalance):
    """ 
    This function calculates a new account balance given an amount to deposit to the account.
    """
    amtToDeposit = getDepositAmount()
    newBalance = accountBalance + amtToDeposit
    return(newBalance)

def getInitialBalance():
    """
    This function asks the user for their savings account balance and returns the amount.
    """
    accountBalance = int(input("How much do you have in your savings account? "))
    return(accountBalance)
    
def getWithdrawlAmount():
    """ This function asks the user for the amount they wish to withdraw and returns the amount.
    """ 
    amtToWithdraw = int(input("How much do you want to withdraw? "))
    return(amtToWithdraw)
    
def getDepositAmount():
    """ This function asks the user for the amount they wish to deposit to their account and returns the amount.
    """ 
    amtToDeposit = int(input("How much do you want to deposit? "))
    return(amtToDeposit)

# function to display menu options
def menuOptions():
    print("Menu Options:")
    print ("""
    1. Withdraw money
    2. Deposit money
    3. Print balance
    4. Quit""")
    
# running the main function
main()



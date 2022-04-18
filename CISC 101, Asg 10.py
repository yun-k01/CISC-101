"""
Yun Kyaw, 20177325
Assignment 10: Mock Final Exam
April 1, 2022
"""
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request

"""
Question 1
"""

def readURLData():
    response = urllib.request.urlopen("https://research.cs.queensu.ca/home/cords2/timHortons.txt")
    html = response.readline()
    
    # dictionaries to hold the orders and the items within the orders
    orders = {}
    items = {}
    
    try: 
        while len(html) != 0:
            data = html.decode('utf-8').split()  
            
            orderNos = data[0]   # selecting the order number
            orderNos = int(orderNos)   # making the order number an integer instead of a string
            
            x = data[1:-1]   # selecting the food items
            y = data[-1]   # selecing the cost 
            y = float(y)   # making the cost a float instead of a string
            
            items = {"food": x, "cost": y}   # assigning the food and cost to the items dictionary
            
            orders[orderNos] = items   # assigning the items dictionary to the orders dictionary for an order number
    
            html = response.readline()
    except:
        print("URL Error")
        return {}
    
    return(orders)
orderDictionary = readURLData()
print(orderDictionary)



"""
Question 2
"""
def orderSum(dictionary):
    """
    this function calculates the average cost of an order and which order is cheaper
    input:
        dictionary - dictionary (keys: integer, values: string + list, string + float)
    return:
        avgCost - float
        cheaper - string
    """
    Costs = []

    # for loop to calculate the average cost of an order
    for i in range(len(dictionary)):
        x = 101 + i
        Costs.append(dictionary[x]["cost"])   # creating a list of the different costs
        
    avgCost = sum(Costs) / len(dictionary)   # calculating the average cost
    
    cheaper = min(Costs)   # determining which of the orders is the cheapest
    
    # for loop to determine which order is the cheapest
    for i in range(len(dictionary)):
        x = 101 + i
        if cheaper == dictionary[x]["cost"]:
            cheapest = x   # selecting the order number
          
    return[avgCost, cheapest]
    


"""
Question 3
"""
def removingCoffeeAndWraps(dictionary):
    """
    this function removes wraps and exchanges coffee for tea from orders
    input:
        dictionary - dictionary (keys: integer, values: string + list, string + float)
    returns:
        dictionary - dictionary (keys: integer, values: string + list, string + float)
    """
    for i in range(len(dictionary)):
        x = 101 + i
        y = dictionary[x]["food"]
        
        # exchanging coffee for tea
        if "Coffee" in y:
            y.remove("Coffee")
            y.insert(0, "Tea")
        
        # removing wraps from orders and making the cost $2.3 less
        if "Wrap" in y:
            y.remove("Wrap")
            dictionary[x]["cost"] -= 2.3
            
    return dictionary



"""
Question 4
"""
def main():
    print("Here is the menu of options:")
    print("""
    1. Update orders
    2. Find average and minimum cost of orders
    3. Insert a new order
    4. Exit this program
    """)
    orderDictionary = readURLData()
    choices = input("What would you like to do? ")
    
    # loop control variable
    loopControl = 0
    while loopControl != 1:
        
        # updating orders to remove wraps and exchange coffee for tea
        if choices == "1":
            orderDictionary = removingCoffeeAndWraps(orderDictionary)
            print("These are the orders:", orderDictionary, sep = "\n")
            choices = input("What would you like to do next? ")
        
        elif choices == "2":
            avgOrder = orderSum(orderDictionary)
            print("The average order is $", avgOrder[0], sep = "")
            print("The cheapest order is order #", avgOrder[1], sep = "")
            choices = input("What would you like to do next? ")
            
        elif choices == "3":
            # adding the order number
            newOrderNos = list(orderDictionary.keys())[-1]
            newOrderNos = int(newOrderNos) + 1
                
            # adding the items to the order
            newOrderFoodNos = int(input("How many items were ordered? "))
            newOrder = {}
            newOrderFoods = []
            for i in range(newOrderFoodNos):
                newFood = input("What was ordered? ")
                newOrderFoods.append(newFood)
                  
            newOrderCost = float(input("How much did it cost? $"))

            newOrder = {"food": newOrderFoods, "cost": newOrderCost}
            orderDictionary[newOrderNos] = newOrder
            3
            
            print("The orders are:", orderDictionary)
            print("\n")
            choices = input("What would you like to do next? ")
        
        elif choices == "4": 
            loopControl = 1
            print("Exiting the program...")
            
        else: 
            choices = input("Invalid input. What would you like to do? ")
            
main()
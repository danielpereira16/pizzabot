# Pizza Bot Program
import random
from random import randint

#List of random names
names = ["Daniel", "Caleb", "Jayden", "Carlos", "Louis", "Keira", "Danett", "Hannah", "Francesca", "Ella" ]

# Welcome messsage with random name
def welcome():
    '''
    Purpose: To generate a random name form the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** my name is ",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")


# Menu for pick up or delivery






# Pick up information - name and phone number






# Delivery information - name address and phone





# Choose total number of Pizzas - max 5






# Pizza Menu






# Pizza order - from menu - print each pizza ordered with cost





# Print order out - including if order is delivering or pick up and names and price of each pizza - total cost including any delivery charge




# Ability to cancel or proceed with order





# Option for new order or to exit




# Main Function
def main():
    '''
    Purpose: To run all functions 
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()


main()
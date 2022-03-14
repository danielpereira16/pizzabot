import random
from random import randint

#List of random names
names = ["Daniel", "Caleb", "Jayden", "Carlos", "Louis", "Keira", "Danett", "Hannah", "Francesca", "Ella" ]

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


def main():
    '''
    Purpose: To run all functions 
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()


main()
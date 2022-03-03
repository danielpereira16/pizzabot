# Pizza Bot Program
#3.03.2022
#Bugs - Phone number input allows letters
#     - Name input allows numbers



import random
from random import randint

#List of random names
names = ["Daniel", "Caleb", "Jayden", "Carlos", "Louis", "Keira", "Danett", "Hannah", "Francesca", "Ella" ]
# Customer details dictionary
customer_details = {}

# validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")


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


#Menu for pickup or delivery
def order_type():
    print ("Is your order for pickup or delivery")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    pickup()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    break
            else: 
                print("Number must be 1 or 2")
        except ValueError:
            print("That is not valid number")
            print("Please enter 1 or 2 ")


# Pick up information - name and phone number
def pickup():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    #print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print(customer_details['phone'])
    print(customer_details)





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
    order_type()
    


main()
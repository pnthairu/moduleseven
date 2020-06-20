# Start Program
"""
""
Program: basic_list.py
Author: Paul Thairu
Last date modified: 06/019/2020

Write the function make_list() that asks for 3 user input in a loop by calls get_input(), returns a string
casts the input to desired type, raising exception on non-numeric input.
After all this is done return the list and call the get_input() in main

"""
# Defining get_input() function
def get_input():
    pass


# Defining make_list() function
def make_list():
    # Declaring a list
    my_numbers = []
    # Declare a number then assigning it get_input function calls
    number = get_input()
    # Looping through a list of three numbers
    for i in range(3):
        # User input prompt to enter the three numbers
        number = (int(input("Please enter your desired number " + str(i+1) + " :")))
        #Assigning the numbers to the list
        my_numbers.append(number)
    # printing the three numbers in  a lists
    print(my_numbers)

    return my_numbers


if __name__ == '__main__':
    make_list() # function call


# End program

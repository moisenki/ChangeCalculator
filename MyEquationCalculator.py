#-------------------------------------------------------------------------------
# Name:        MyEquationCalculator.py
# Purpose:     Takes user input of a string in the form of operand, operator,
#              operand, and computes the two operands based on the operator.
#              Supports addition, multiplication, subtraction, and division.
#
# Author:      gleb
#
# Created:     01-02-2016
# Copyright:   (c) gleb 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Hello! \nThis program accepts input in the form [Number operator Number], and will compute the result.\nSupported operators are ['plus' 'minus' 'times' 'divided-by']. Make sure to put a space inbetween each item.")

# Set variables
#opList = ["plus", "minus", "times", "divided-by"]

# Read user's equation as a string
equation = raw_input("\nPlease, enter your equation by following the syntax expressed above: ")

# Echo to the screen what the user has entered
print('\nThe equation you entered is "%s".' %equation)

# Parse the equation into a list
theParts = equation.split() # default is whitespace
# print("Here is a list containing the operands and operator of the equation: ", theParts) # For debugging purposes

if len(theParts) == 0 :
    print("\nHave you simply pressed the Enter key? Please, enter an equation next time! :)")

elif len(theParts) == 1 :
    print("\nInsufficient input for meaningful answer!") # Print a descriptive message

elif len(theParts) == 2 :
    print("\nInsufficient input for meaningful answer!") # Print a descriptive message

elif len(theParts) == 3 :  # Valid equation, compute it and prints its result.
    print("")

# Assigns the list to individual variables, the 2 operators and the operand
    operand1 = float(theParts[0])
    operator = theParts[1]
    operand2 = float(theParts[2])

# Computes result based on operator
    if operator == "plus":
        result = operand1 + operand2

    elif operator == "minus":
        result = operand1 - operand2

    elif operator == 'times':
        result = operand1 * operand2

    elif operator == "divided-by":
        result = operand1 / operand2

    else:
        print("Please input proper operator")


# For debug purposes - We can index a list just like a string using [index]
        print("\nThe equation entered by the user is %s %s %s." %(theParts[0], theParts[1], theParts[2]))

# The result is printed
    print("The result is %s" %result)

# If the number of inputs exceeds 4, this error message will be prompted
else:
    print("\nToo many items entered! Please only enter 3")

# Program finishes with farewell message
print("\nBye!")

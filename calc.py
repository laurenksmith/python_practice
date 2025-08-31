# basic calc

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


choice = int(input('\n Enter 1 for addition and 2 for subtraction: ')) # \n means input a new line

num1 = int(input('\n Input your first number: '))
num2 = int(input('\n Input your second number: '))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == 2:
    print(num1, '-', num2, '=', subtract(num1, num2))
else:
    print('Invalid choice.') # I would want this to be before it lets the user input their numbers.

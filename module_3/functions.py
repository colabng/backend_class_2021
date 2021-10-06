"""A function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, 
functions make it more organized and manageable.
"""

def greet():
    print('Good morning')

greet()

def greet(name):
    print('Good morning', name)

greet('Abdul')

#function without a parameter
def my_function():
    first_num = 2
    second_num = 2
    print((first_num + second_num)*10)

my_function()

#function with a parameter
def my_function_param(first_num, second_num):
    print((first_num + second_num)*10)

my_function_param(6,7)
my_function_param(5,4)

def odd_even_checker(number):
    if number % 2 == 0:
        print('Even Number')
    else:
        print('Odd Number')

odd_even_checker(2)
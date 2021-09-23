"""
    DATA TYPES
        - Primitive datatypes
            - integers: 1, 2, 3, 4
            - floats: 2.4, 2.5
            - strings: 'nyior', "4"
            - boolean: True, False

        - Other datatypes
            - Lists(called arrays in other programmig languages)
            - Dicionaries
            - Tuples

        - Flow COntrols
            - if-elif-else
        Looops
         - For and while
"""

# creating a list
numbers = [1, 2, 3, 4]
cities_and_numbers = ["kaduna", "Abuja", 10, "12"]
print(cities_and_numbers)

# operations on a list. These operations could also be performed on strings
len(numbers) # returns the size of the list
numbers[0]  # retrieving based on index
numbers[1:] # slicing 

name = "Adebayo"
name[0]
cities_and_numbers.append("Lagos") # adds item to the end of the list
cities_and_numbers.append("100")
print(cities_and_numbers)

cities_and_numbers.pop() # remove the last item
cities_and_numbers.pop()
print(cities_and_numbers)

cities_and_numbers.remove("kaduna") # remove a specific value
print(cities_and_numbers)

cities_and_numbers.pop(0) # remove based on index
print(cities_and_numbers)

# Creating a new dictionary
user_data = {
    "name": "Gabriel", 
    "age": "12", 
    "state": "kaduna"
}

users_data = {
    1: {
        "name": "Gabriel", 
        "age": "12", 
        "state": "kaduna"
    },

    2:  {
        "name": "Angel", 
        "age": "12", 
        "state": "Lagos"
    }
}

user_data["name"] # retrieving an item from a dictionary
users_data[1]

user_data["address"] = "Kamazou" # adding to a dictionary

user_data.pop("name") # removing an entry from a dictionary

names = ("nyior", "clement",) # read more on tuples


# If else blocks in Python

if name == "Sam":
    print("right!")
elif name == "Gabriel":
    print("right again")
elif name == "Bill":
    print("right again")
else:
    print("wrong")


if name == "Sam" or name == "Gabriel" or name == "Bill":
    print("right!")

else:
    print("wrong")


# While Loops in Python

number = 0

while number < 10: 
    print("number still less than 10")
    number += 1
    print(f"number is now: {number} ")


numbers = [1, 2, 3, 4]

for item in numbers:
    print(item)

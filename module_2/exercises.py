"""
    For now familiarize yourselves with operations on strings and lists
    Learn about dictionaries and tuples 

    Do sturvs here to demonstrate what you've learnt and open a pull request.
"""

"""
    DICTIONARIES:
        -dictionaries are created using curly brackets
        -printing out the name of a variable with a key name inside a square bracket selects the item that has the given key name
"""
# Dictionary example
phone = {
    "product": "Iphone",
    "color": "skyblue"
}
print(phone)

# Selecting a single item by using the key name inside a square bracket []
person = {
    "first_name": "Daniel",
    "last_name": "Mathew"
}
print(person["last_name"])




"""
    TUPPLES:
        -turple is used to store multiple items in a single variable
        -a turple is a collection which is ordered and unchangeable.
        -a turple can contain different data types(strings, integers and boolean)
"""
# example of a turple
fruits = ("cherry","banana","apple")
print(fruits)

# a turple with data types
school = ("teachers", 13, "True")
print(school)




"""
    LISTS:
        -lists are used to store multiple items in a single varianble
        -lists are created using square brackets []
"""
# example of lists
fruit_list = ["apple", "banana", "orange", "cherry"]
print(fruit_list)
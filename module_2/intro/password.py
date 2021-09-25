
# Handling incorrect passwords scenario with loops
correct_password = "Gabriel"

password = input("Type in your password: ")

while password != correct_password:
    password = input("Wrong password. TRY AGAIN: ")

print("SUCCESSFULLY LOGGED IN")

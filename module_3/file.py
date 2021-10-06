#open a file
f = open("test.txt", "r")

#read the content of the file
content = f.read()
print(content)

#close an opened file
f.close()

with open("test1.txt",'w') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")


"""file modes
a: Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
x: Opens a file for exclusive creation. If the file already exists, the operation fails.
w: Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
r: Opens a file for reading.

"""
# File Handling && Exception Handling
import os

  # Opening file
# f = open("note.txt")
# print(f.read(5))
# f.close()


# with open("note.txt") as f:
#   print(f.readline())
#   print(f.readline())


# with open("note.txt") as f:
#   for x in f:
#     print(x)

# f = open("/home/ceasar/changes.txt")
# print(f.read())
# f.close()


# with open("/home/ceasar/changes.txt") as f:
#   print(f.read())


# Write file
# with open("note.txt", "a") as f:
 
#   f.write("Today we are diving on exception handling")


# with open("note.txt") as f:
#   print(f.read())


# with open("note.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("note.txt") as f:
#   print(f.read())  
  

# Creating new file
# f = open("myfile.txt", "x")  
# with open("myfile.txt", "a") as f:
 
#   f.write("Today we are diving on exception handling")


# Delete file

# if os.path.exists("myfile.txt"):
#   os.remove("myfile.txt")
# else:
#   print("The file does not exist")

# Delete folder

if os.path.exists("myfolder"):
  os.rmdir("myfolder")
else:
  print("The folder does not exist")
  
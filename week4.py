with open ("dave.txt","r") as file:
    content=file.read()
with open ("dave.txt","w") as file:
    file.write("this is damn easy")

try:
    username=input("username")
except FileNotFoundError:
    pass


File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
Outcomes 🎉
#imports argv from sys
from sys import argv

#unpacks argv
script, filename = argv

#opens the file from the commandline and saves it in a vsariable called txt
txt = open(filename)

#prints put including the filename
print(f"Here's your file {filename}:")

#reads the opened txt file and prints the contents of the file
print(txt.read())

file_again = input("Type the filename again:\n> ")

print("Type the filename again:")

file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

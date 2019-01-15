from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv

print("The script is called:", script)

print("Your first variable is:", first)

print("Your second variable is:", second)

print("Your third variable is:", third)

lastz = input("how may metres? ")

x = int(lastz)

if x > 100:
    print("wow thats a lot")
elif x < 20:
    print("thats too few")
else:
    print("good")

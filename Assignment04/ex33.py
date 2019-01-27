#While-Loops
#A while-loop will keep executing the code block under it as long as a boolean
#expression is True.

#1. Make sure that you use while-loops sparingly. Usually a for-loop is better.

#2. Review your while statements and make sure that the boolean test will become
#False at somepoint.

#3. When in doubt, print out your test variable at the top and bottom of the
#while-loop to see what it’s doing.

i = 0

numbers = []

for i in range(0, 6):
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

#def listed(max, zz):
#    i = 0
#    numbers = []
#    while i < max:
#        print(f"At the top i is {i}")
#        numbers.append(i)
#        i = i + zz
#        print("Numbers now: ", numbers)
#        print(f"At the bottom i is {i}")
#    print("The numbers: ")
#
#    for num in numbers:
#        print(num)
#
#listed(10000, 20)

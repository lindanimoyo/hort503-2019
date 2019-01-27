#Loops and Lists

#However, programs also need to do repetitive things very quickly.

#for-loop

#Before you can use a for-loop, you need a way to store the results of loops somewhere.
#The best way to do this is with lists.

#Lists are exactly what their name says: a container of things that are organized
#in order from first to last.

hairs = ['brown', 'blond' , 'red']

for member in hairs:
    print(member + ".com")

hairs

print(hairs)

eyes = ['brown', 'blue' , 'green']

print(eyes)

weights = [ 1 , 2 , 3 , 4 ]

for x in weights:
    print(f" this is the number in set wieghts: {x}")

x = "lindan"

a = int(45)

print(x)

print(a)

#WARNING! This is where things get tricky for people who can’t code. Your brain has
#been taught that the world is flat. Remember in the last exercise where you put if-statements
#inside if-statements? That probably made your brain hurt because most
#people do not ponder how to ”nest” things inside things. In programming nested structures
#are all over the place. You will find functions that call other functions that have
#if-statements that have lists with lists inside lists. If you see a structure like this that
#you can’t figure out, take out a pencil and paper and break it down manually bit by bit
#until you understand it.

the_count = [1, 2, 3, 4, 5]

fruits = ['apples', 'oranges', 'pears', 'apricots']

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")

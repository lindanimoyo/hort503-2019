#Loops and Lists
#for-loop

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

dividends = []

for x in the_count:
    y = x / 2
    dividends.append(y)
    print(dividends)

print(dividends)


fruits = ['apples', 'oranges', 'pears', 'apricots']

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")


# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it

for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

for x in range(5, 9):
    elements.append(x)

# now we can print them out too
print(elements)
for z in elements:
    print(f"Element was: {z}")

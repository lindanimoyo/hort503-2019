#if-statement ....conditional statements using boolean expressions.
#The if-statement tells your script, ”If this Boolean expression is True,
#then run the code under it, otherwise skip it.”
#executes the code under it, if the condition is true
#hence changing the values of the variables in the statement changes the result
#of the condition such that code below may not be executed
#indent makes the code part of the if statement

#a colon creates a block of code

people = 20

cats = 30

dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

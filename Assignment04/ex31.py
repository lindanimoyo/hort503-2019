#In the first half of this book you mostly just printed out things called functions,
#but everything was basically in a straight line. Your scripts ran starting at the
#top and went to the bottom where they ended. If you made a function, you could run
#that function later, but it still didn’t have the kind of branching you need to
#really make decisions.

#Lindani Moyo

#Now that you have if, else, and elif you can start to make scripts that decide things.

#A key point here is that you are now putting the if-statements inside if-statements as
#code that can run. This is very powerful and can be used to create ”nested” decisions,
#where one branch leads to another and another.

#combine all the other things you have learned with if-statements and boolean expressions
#to make your programs do smart things.

print("""You enter a dark room with two doors. Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
        print("better clean the floor, how do we clean it?")
        print("1. use acid.")
        print("2. use dawn.")

        cleaner = input("> ")

        if cleaner == "1":
            print("cleaner wipes your existence")
        elif cleaner == "2":
            print("cleaner does a messy job, law will trace your killer")
        else:
            print("we a cleaner")

    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")


elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")

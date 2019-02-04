#Modules, Classes, and Objects
#class that lets you structure your software in a particular way

#Modules Are Like Dictionaries
#You know how a dictionary is created and used and that it is a way to map one
#thing to another. That means if you have a dictionary with a key ”apple” and
#you want to get it then you do this:

#A class is a way to take a grouping of functions and data and place them inside
#a container so you can access them with the . (dot) operator.

class Song(object):

    def __init__(self, lyrics, chorus):
        self.lyrics = lyrics #attaches data to the object
        self.sing_chorus = chorus

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            print(f" singing:> {self.sing_chorus}")

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"],
                   ["hello", "helloe", "ohhhhh"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"],
                        ["daaa", "all the way"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

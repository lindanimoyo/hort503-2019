## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    pass

#dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        #Dog has-a name
        self.name = name

#cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##cat has-a name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        #person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

#Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

#salmom is-a fish
class Salmon(Fish):
    pass

#halibut is-a fish
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")

#sat is-a cat
sat = Cat("Sat")

#Mary is person
mary = Person("Mary")

#mary has-a pet called sat that is-a cat
mary.pet = sat

#frank has-a name and salary
frank = Employee("Frank", 120000)

#frank has-a pet called rover that is-a dog
frank.pet = rover

#Flipper is-a fish
flipper = Fish()

#crouse is salmon is a fish
crouse = Salmon()

#harry is halibut is a fish
harry = Halibut()

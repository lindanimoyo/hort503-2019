
# Implicit Inheritance
# Very handy for repetitive code you need in many classes.

class Parent(object):
    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass

dad = Parent()

son = Child()

dad.implicit()

son.implicit()


# Override Explicitly
# sometimes you want the child to behave differently
# just define a function with the same name in Child

# function named override in both classes

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()

son = Child()

dad.override()

son.override()

# Alter Before or After
# inheritance is a special case of overriding where you want to alter the behavior
# before or after the Parent class’s version runs
# use a Python built-in function named super to get the Parent version to call

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()

son = Child()

dad.altered()

son.altered()

# All Three Combined

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()

son = Child()

dad.implicit()

son.implicit()

dad.override()

son.override()

dad.altered()

son.altered()

# multiple inheritance
# define a class that inherits from one or more classes

# Composition
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()

son.override()

son.altered()

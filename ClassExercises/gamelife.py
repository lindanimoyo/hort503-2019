
#create a class called cell

class Cell(object):
    """cell class"""
    def __init__(self, x, y, state):
        self.x = x  # XXX:
        self.y = y
        self.state = state

        if self.state >= 2:
            print("need to type 1 or 0 as your third argument")

        if type(self.state) != int:
            print("type an integer for your first and second argument print")

        if type(self.x) != int:
            print("type an integer for your first and second argument print")

        if type(self.y) != int:
            print("type an integer for your first and second argument print")

    def get_state(self):
        return self.state


    def set_state(self, state):
        self.state = state
        if self.state >= 2:
            print("need to type 1 or 0 as your third argument")
        if type(self.state) != int:
            print("type an integer for your first and second argument print")

game = Cell(3, "a", 1)

game.set_state(1)

game.get_state()

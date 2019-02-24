
#create a class called cell
class Cell(object):
    """cell class"""
    def __init__(self, x, y, state):
        self.x = x
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

def test_cell():
    game = Cell(3, 2, 0)
    print(game.get_state())
    game.set_state(1)
    print(game.get_state())

test_cell()

#create class called grid
class Grid(object):
    """cell Grid"""
    def __init__(self, grid, rows, cols):
        self.grid = grid
        self.rows = rows
        self.cols = cols

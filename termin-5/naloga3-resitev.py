class Robot:
    def __init__(self, grid, position, destination, visited):
        self.grid = grid
        self.position = position
        self.destination = destination
        self.visited = []

    def solved(self):
        """ Returns true if the current position is the destination. """
        return False

    def move(self, move):
        pass


def main():
    """
    Trije testni gridi:

    grid = [ [0,0,0,0,0,0],
             [1,0,1,1,1,0],
             [0,0,1,0,0,0],
             [0,1,1,0,0,0],
             [0,1,0,0,0,0],
             [0,0,0,0,0,0]]

    grid = [ [0,0,0,0,0,0],
             [1,1,1,1,1,0],
             [1,0,1,0,0,0],
             [1,1,1,0,0,0],
             [0,1,0,0,0,0],
             [0,0,0,0,0,0]]

    grid = [ [0,0,0,0,0,0,0,1,1,1],
             [1,1,1,0,1,0,0,1,0,0],
             [1,0,0,0,1,0,0,1,0,1],
             [0,0,1,0,0,0,1,1,1,1],
             [1,0,0,0,1,1,1,0,0,1],
             [1,1,0,1,1,0,0,1,0,0],
             [1,0,0,0,1,0,0,0,0,0],
             [1,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,1,0,0,0,0]]
    """
    pass

if __name__ == "__main__":
    main()

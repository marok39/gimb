class Robot:
    def __init__(self, grid, position, destination):
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

    max_depth = len(grid)*len(grid[0])
    for depth in range(max_depth):
        result = check_near((9, 9), (2, 2), grid, depth)
        if result:
            break
    print(result, depth, grid)


def check_near(location, destination, grid, depth):
    if not ((0 <= location[0] < len(grid)) and (0 <= location[1] < len(grid[0]))):
        return False
    if grid[location[0]][location[1]] == 1:
        return False
    if location == destination:
        return True
    if depth == 0:
        return False
    grid[location[0]][location[1]] = 1
    if check_near((location[0]-1, location[1]), destination, grid, depth-1):
        return True
    if check_near((location[0], location[1]-1), destination, grid, depth-1):
        return True
    if check_near((location[0]+1, location[1]), destination, grid, depth-1):
        return True
    if check_near((location[0], location[1]+1), destination, grid, depth-1):
        return True
    return False



if __name__ == "__main__":
    main()

from pprint import PrettyPrinter

class Robot:
    def __init__(self, grid, position, destination):
        self.grid = grid
        self.position = position
        self.destination = destination
        self.visited = []

    def solved(self):
        """ Returns true if the current position is the destination. """
        return self.position == self.destination

    def move(self, move):
        self.visited.append(self.position[:])
        self.position[0] += move[0]
        self.position[1] += move[1]

    def undo_move(self, move):
        self.position[0] -= move[0]
        self.position[1] -= move[1]

    def execute_path(self, path):
        for move in path:
            self.move(move)

    def undo_path(self, path):
        for move in reversed(path):
            self.undo_move(move)

    def generate_moves(self):
        row, col = self.position
        possible_moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
        valid_moves = []
        for dr, dc in possible_moves:
            if  0 <= dr + row < len(self.grid) and \
                0 <= dc + col < len(self.grid[dr + row]) and \
                not self.grid[dr + row][dc + col] and \
                [dr + row, dc + col] not in self.visited:
                valid_moves.append([dr, dc])
        return valid_moves

    def DF(self, depth=100):
        if depth < 0: # cycle detection
            return None
        if self.solved():
            return []
        for move in self.generate_moves():
            self.move(move)
            path = self.DF(depth - 1)
            self.undo_move(move)
            if path != None:
                return [move] + path
        return None

    def BF_helper(self, paths):
        path = paths.pop(0)
        self.execute_path(path)
        if self.solved():
            self.undo_path(path)
            return path
        for move in self.generate_moves():
            paths.append(path + [move])
        self.undo_path(path)
        return None

    def BF(self):
        paths = [[]]
        while paths:
            path = self.BF_helper(paths)
            if path != None:
                return path
        return None


def show_path(grid, path, start, end):
    r, c = start
    grid[r][c] = 'o'
    for dr, dc in path[:-1]:
        r += dr
        c += dc
        grid[r][c] = '.'
    r, c = end
    grid[r][c] = 'x'
    return grid

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
    pp = PrettyPrinter(indent=2)

    grid = [ [0,0,0,0,0,0],
             [1,0,1,1,1,0],
             [0,0,1,0,0,0],
             [0,1,1,0,0,0],
             [0,1,0,0,0,0],
             [0,0,0,0,0,0]]

    start = [5, 5]
    end = [2, 1]
    r = Robot(grid, start, end)
    result = r.BF()
    #result = r.DF()
    pp.pprint(result)
    # pp.pprint(r.visited)
    pp.pprint(show_path(grid, result, start, end))
    pp.pprint(len(result))

if __name__ == "__main__":
    main()

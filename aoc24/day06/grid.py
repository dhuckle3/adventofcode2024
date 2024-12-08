import doctest
from collections import defaultdict
from itertools import cycle
from enum import Enum
from copy import deepcopy


class Direction(Enum):
    __order__ = "UP RIGHT DOWN LEFT"
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


class Guard(Enum):
    CYCLE = -1
    CONTINUE = 0
    COMPLETE = 1


class Grid:
    """
    Example Grid
    >>> data = "..#.\\n..^#\\n#...\\n..#."
    >>> grid = Grid(data)
    >>> print(grid)
    ..#.
    ..^#
    #...
    ..#.
    >>> grid.facing == Direction.DOWN
    True
    >>> grid.patrol() == Guard.COMPLETE
    True
    >>> grid.count_x()
    5
    """

    def __init__(self, data):
        self.grid = []
        for y, line in enumerate(data.split("\n")):
            if len(line) == 0:
                continue
            if "^" in line:
                try:
                    x = line.index("^")
                    self.pos = (x, y)
                except ValueError:
                    sys.exit(1)
            self.grid.append(list(line))
        self.set(self.pos, 1)
        self.facing = Direction.UP
        self.update_facing()

    def patrol(self):
        result = Guard.CONTINUE
        while result == Guard.CONTINUE:
            result = self.move()
        return result

    def rotate(self):
        """
        >>> g = Grid("^")
        >>> g.facing == Direction.UP
        True
        >>> g.rotate()
        >>> g.rotate()
        >>> g.rotate()
        >>> g.rotate()
        """
        dirs = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        self.facing = dirs[(dirs.index(self.facing) + 1) % 4]

    def move(self):
        next_pos = self.get_next_pos()
        if self.outside(next_pos):
            self.pos = None
            return Guard.COMPLETE
        else:
            self.pos = next_pos
            if isinstance(self.get(self.pos), str):
                self.set(self.pos, 0)
            self.set(self.pos, self.get(self.pos) + 1)
            self.update_facing()

            if self.get(self.pos) > 9:
                return Guard.CYCLE
            else:
                return Guard.CONTINUE

    def update_facing(self):
        next_pos = self.get_next_pos()
        if self.outside(next_pos):
            return

        if self.get(next_pos) == "#":
            self.rotate()
            # call update facing again as we might need to rotate multiple times
            self.update_facing()

    def get_next_pos(self):
        """
        return the next square the guard will attempt to move to even if that
        move is not possible and the guard will end up rotating. Does not
        change any state.

        >>> g = Grid("##\\n^#\\n.#\\n")
        >>> print(g)
        ##
        ^#
        .#
        >>> g.facing == Direction.DOWN
        True
        >>> g.get_next_pos()
        (0, 2)
        """
        return tuple(a + b for a, b in zip(self.pos, self.facing.value))

    def outside(self, pos):
        (x, y) = pos
        if x < 0 or y < 0 or x >= len(self.grid[0]) or y >= len(self.grid):
            return True
        return False

    def count_x(self):
        total = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if isinstance(self.get((x, y)), int):
                    total = total + 1
        return total

    def get(self, pos):
        (x, y) = pos
        return self.grid[y][x]

    def set(self, pos, value):
        (x, y) = pos
        self.grid[y][x] = value

    def __str__(self):
        copy = deepcopy(self.grid)
        for y in range(len(copy)):
            for x in range(len(copy[y])):
                if type(copy[y][x]) == int:
                    copy[y][x] = str(self.get((x, y)))
        if self.pos != None:
            (x, y) = self.pos
            copy[y][x] = "^"
        res = []
        for y in range(len(copy)):
            res.append("".join(copy[y]))
        return "\n".join(res)


if __name__ == "__main__":
    doctest.testmod()

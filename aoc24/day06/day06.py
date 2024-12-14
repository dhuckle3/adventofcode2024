import sys
from grid import Grid
from grid import Guard
from copy import deepcopy


def part1(input):
    """ """
    g = Grid(input)
    g.patrol()
    return g.count_x()


def part2(input):
    grid = Grid(input)
    initial = deepcopy(grid)
    check = set()

    result = Guard.CONTINUE
    while result == Guard.CONTINUE:
        result = grid.move()
        if grid.pos is not None:
            check.add(grid.pos)

    locations = 0
    for i, pos in enumerate(check):
        temp_grid = deepcopy(initial)
        temp_grid.set(pos, "#")
        temp_grid.update_facing()
        res = temp_grid.patrol()
        if res == Guard.CYCLE:
            locations = locations + 1
    return locations


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("data/day06/input").read()
    print("part1:", part1(file))
    print("part2:", part2(file))

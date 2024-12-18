import sys
from collections import defaultdict
from itertools import combinations


def parse_input(input):
    """
    >>> (d, x, y) = parse_input("............\\n........0...\\n.....0......");
    >>> x
    12
    >>> y
    3
    """
    antennas = defaultdict(set)
    for y, line in enumerate(input.split("\n")):
        for x, character in enumerate(line):
            if character != ".":
                antennas[character].add((x, y))
    height = len(input.split("\n"))
    width = len(input.split("\n")[0])
    return (antennas, width, height)


def part1(input):
    """ """
    antennas = defaultdict(set)
    antinodes = defaultdict(set)
    grid = []
    for y, line in enumerate(input.split("\n")):
        grid.append(list(line))
        for x, character in enumerate(line):
            if character != ".":
                antennas[character].add((x, y))

    height = len(input.split("\n")) - 1  # garbage handling of NL at EOF
    width = len(input.split("\n")[0])
    print(width, height)

    for key in antennas.keys():
        for pair in list(combinations(antennas[key], 2)):
            (a1, a2) = find_antinodes_part1(pair[0], pair[1])
            if in_bounds(a1, width, height):
                antinodes[key].add(a1)
            if in_bounds(a2, width, height):
                antinodes[key].add(a2)
    count = set()
    for key in antinodes.keys():
        count.update(antinodes[key])

    for node in count:
        (x, y) = node
        if in_bounds(node, width, height):
            grid[y][x] = "#"

    for line in grid:
        print("".join(line))
    return len(count)


def in_bounds(point, x, y):
    """
    >>> in_bounds((0, 0), 10,10)
    True
    >>> in_bounds((9, 9), 10,10)
    True
    """
    return point[0] >= 0 and point[0] < x and point[1] >= 0 and point[1] < y


def part2(input):
    """ """
    antennas = defaultdict(set)
    antinodes = defaultdict(set)
    grid = []
    for y, line in enumerate(input.split("\n")):
        grid.append(list(line))
        for x, character in enumerate(line):
            if character != ".":
                antennas[character].add((x, y))

    height = len(input.split("\n")) - 1  # garbage handling of NL at EOF
    width = len(input.split("\n")[0])
    print(width, height)

    for key in antennas.keys():
        for pair in list(combinations(antennas[key], 2)):
            nodes = find_antinodes_part2(pair[0], pair[1], width, height)
            for node in nodes:
                if in_bounds(node, width, height):
                    antinodes[key].add(node)
    count = set()
    for key in antinodes.keys():
        count.update(antinodes[key])

    for node in count:
        (x, y) = node
        if in_bounds(node, width, height):
            grid[y][x] = "#"

    for line in grid:
        print("".join(line))
    return len(count)


def find_antinodes_part1(p1, p2):
    """
    >>> find_antinodes_part1((10,10), (11, 12))
    [(9, 8), (12, 14)]
    >>> find_antinodes_part1((11, 12), (10, 10))
    [(12, 14), (9, 8)]
    >>> find_antinodes_part1((4,3), (5,5))
    [(3, 1), (6, 7)]
    >>> find_antinodes_part1((5, 2), (8, 1))
    [(2, 3), (11, 0)]
    """
    diff = tuple(a - b for a, b in zip(p1, p2))
    a1 = tuple(a + b for a, b in zip(p1, diff))
    a2 = tuple(a - 2 * b for a, b in zip(p1, diff))
    return [a1, a2]


def find_antinodes_part2(p1, p2, x, y):
    """ """
    nodes = set()
    diff = tuple(a - b for a, b in zip(p1, p2))
    node = p1
    while True:
        node = tuple(a + b for a, b in zip(node, diff))
        if not in_bounds(node, x, y):
            break
        nodes.add(node)

    # adjust to not include p2?
    while True:
        node = tuple(a - b for a, b in zip(node, diff))
        if not in_bounds(node, x, y):
            break
        nodes.add(node)

    return nodes


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("data/day08/input").read()
    print("part1:", part1(file))
    print("part2:", part2(file))

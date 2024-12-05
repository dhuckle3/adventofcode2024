import sys


def make_list(input):
    """
    >>> make_list(["abc","def", "ghi"])
    [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    """
    result = []
    for line in input:
        result.append(list(line))
    return result


def find_xmas(map):
    """ """
    count = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "X":
                count = count + check_eight_dirs(map, x, y)
    return count


def check_eight_dirs(map, x, y):
    count = 0
    if chk(map, x + 1, y, "M") and chk(map, x + 2, y, "A") and chk(map, x + 3, y, "S"):
        count = count + 1
    if chk(map, x - 1, y, "M") and chk(map, x - 2, y, "A") and chk(map, x - 3, y, "S"):
        count = count + 1
    if chk(map, x, y + 1, "M") and chk(map, x, y + 2, "A") and chk(map, x, y + 3, "S"):
        count = count + 1
    if chk(map, x, y - 1, "M") and chk(map, x, y - 2, "A") and chk(map, x, y - 3, "S"):
        count = count + 1
    if (
        chk(map, x + 1, y + 1, "M")
        and chk(map, x + 2, y + 2, "A")
        and chk(map, x + 3, y + 3, "S")
    ):
        count = count + 1
    if (
        chk(map, x - 1, y - 1, "M")
        and chk(map, x - 2, y - 2, "A")
        and chk(map, x - 3, y - 3, "S")
    ):
        count = count + 1
    if (
        chk(map, x + 1, y - 1, "M")
        and chk(map, x + 2, y - 2, "A")
        and chk(map, x + 3, y - 3, "S")
    ):
        count = count + 1
    if (
        chk(map, x - 1, y + 1, "M")
        and chk(map, x - 2, y + 2, "A")
        and chk(map, x - 3, y + 3, "S")
    ):
        count = count + 1
    return count


def check_cross_xmas(map, x, y):
    if (
        chk(map, x + 1, y + 1, "M")
        and chk(map, x - 1, y - 1, "S")
        and chk(map, x + 1, y - 1, "M")
        and chk(map, x - 1, y + 1, "S")
    ):
        return True
    if (
        chk(map, x + 1, y + 1, "M")
        and chk(map, x - 1, y - 1, "S")
        and chk(map, x + 1, y - 1, "S")
        and chk(map, x - 1, y + 1, "M")
    ):
        return True
    if (
        chk(map, x + 1, y + 1, "S")
        and chk(map, x - 1, y - 1, "M")
        and chk(map, x + 1, y - 1, "M")
        and chk(map, x - 1, y + 1, "S")
    ):
        return True
    if (
        chk(map, x + 1, y + 1, "S")
        and chk(map, x - 1, y - 1, "M")
        and chk(map, x + 1, y - 1, "S")
        and chk(map, x - 1, y + 1, "M")
    ):
        return True
    return False


def chk(map, x, y, letter):
    """
    >>> m = [['a', 'b', 'c'], ['d', 'e', 'f']]
    >>> chk(m, 1, 3, "A")
    False
    >>> chk(m, 2, 1, "f")
    True
    """
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return False
    return map[y][x] == letter


def part1(input):
    """ """
    m = make_list(input)
    return find_xmas(m)


def part2(input):
    """ """
    m = make_list(input)
    count = 0
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "A":
                count = count + check_cross_xmas(m, x, y)
    return count
    return None


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("input").readlines()
    print("part1:", part1(file))
    print("part2:", part2(file))

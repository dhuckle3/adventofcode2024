import sys


def part1(input):
    """
    >>> part1("")
    """
    return None


def part2(input):
    """
    >>> part2("")
    """
    return None


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("data/day00/input").read()
    print("part1:", part1(file))
    print("part2:", part2(file))

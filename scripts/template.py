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

    file = open("input").read()
    part1(file)
    part2(file)

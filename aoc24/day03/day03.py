import sys
import re


def part1(input):
    """
    >>> part1("mul(2,3)")
    6
    """
    return find_mul(input)


def find_mul(line):
    """
    >>> find_mul("asdfmul(2,3)asdf")
    6
    >>> find_mul("asdfasdf")
    0
    >>> find_mul("mul(2,3)mul(3,4)")
    18
    """
    m = re.search("mul\\(([0-9]+),([0-9]+)\\)", line[0 : len(line)])
    if m is None:
        return 0
    else:
        return int(m.group(1)) * int(m.group(2)) + find_mul(line[m.end(0) : len(line)])


def part2(input):
    """
    >>> part2("mul(1,2)don't()mul(1,2)do()mul(2,3)")
    8
    """
    return handle_line(input)


def find_next_section(line):
    """
    Find the next 'do()' and then call handle on it. If there aren't any for
    the remainder of the string, then just return 0
    """
    try:
        i = line.index("do()")
        return handle_line(line[i : len(line)])
    except ValueError:
        return 0


def handle_line(line):
    try:
        i = line.index("don't()")
        return find_mul(line[0:i]) + find_next_section(line[i : len(line)])
    except ValueError:
        return find_mul(line)


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("input").read()
    print("part1:", part1(file))
    print("part2:", part2(file))

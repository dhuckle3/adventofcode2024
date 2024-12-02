import sys


def part1(input):
    """
    >>> part1(["123 124"])
    1
    """
    [left, right] = make_lists(input)
    left.sort()
    right.sort()

    amt = 0
    for i in range(len(left)):
        amt = amt + abs(left[i] - right[i])
    return amt


def part2(input):
    """
    >>> part2(["1 2", "2 2"])
    4
    """
    (left, right) = make_lists(input)
    amt = 0
    for num in left:
        amt = amt + num * len([n for n in right if n == num])

    return amt


def make_lists(input):
    """
    i = "1 1\n2 2\n3 3"
    make_list(i)
    ([1, 2, 3], [1, 2, 3])
    """
    left = []
    right = []

    for line in input:
        [raw_left, raw_right] = line.split()
        left.append(int(raw_left))
        right.append(int(raw_right))
    return (left, right)


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("aoc24/day01/input").readlines()
    print("part1:", part1(file))
    print("part2:", part2(file))

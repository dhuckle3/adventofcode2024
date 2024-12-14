import sys
from copy import copy


def part1(input):
    """
    >>> part1("190: 10 19\\n190: 10 18")
    190
    """
    total = 0
    for line in input.split("\n"):
        if len(line) == 0:
            continue

        (desired, nums) = parse_line(line)
        combos = build_combos_part1(len(nums) - 1)
        if validate(desired, nums, combos):
            total = total + desired
    return total


def parse_line(line: str):
    """
    >>> line = "190: 10 19"
    >>> parse_line(line)
    (190, [10, 19])
    """
    parts = line.split(":")
    total = int(parts[0].strip())
    nums = [int(num) for num in parts[1].strip().split(" ")]
    return (total, nums)


def validate(total: int, nums: list[int], combos: set[str]) -> bool:
    """
    >>> validate(12, [2, 6], {'m', 'p'})
    True
    >>> validate(12, [2, 6, 2], {'mp', 'pm'})
    False
    """
    for combo in combos:
        result = do_combo(combo, copy(nums))
        if result == total:
            return True
    return False


def do_combo(combo: str, nums: list[int]):
    """
    >>> do_combo("pm", [81, 40, 27])
    3267

    """
    if len(combo) == 0:
        return nums[0]

    if combo[0] == "p":
        nums[1] = nums[0] + nums[1]
        return do_combo(combo[1:], nums[1:])
    elif combo[0] == "m":
        nums[1] = nums[0] * nums[1]
        return do_combo(combo[1:], nums[1:])
    else:
        nums[1] = int(str(nums[0]) + str(nums[1]))
        return do_combo(combo[1:], nums[1:])


def build_combos_part1(count: int) -> set[str]:
    """
    >>> result = build_combos_part1(2)
    >>> sorted(result)
    ['mm', 'mp', 'pm', 'pp']
    """
    result = set()
    add_mult(count, "", result, False)
    add_plus(count, "", result, False)
    return result


def build_combos_part2(count: int) -> set[str]:
    """
    >>> result = build_combos_part2(2)
    >>> sorted(result)
    ['cc', 'cm', 'cp', 'mc', 'mm', 'mp', 'pc', 'pm', 'pp']
    """
    result = set()
    add_mult(count, "", result, True)
    add_plus(count, "", result, True)
    add_concat(count, "", result)
    return result


def add_mult(count: int, chain: str, result: set[str], concat: bool):
    if count == 0:
        result.add(chain)
    else:
        add_mult(count - 1, chain + "m", result, concat)
        add_plus(count - 1, chain + "m", result, concat)
        if concat:
            add_concat(count - 1, chain + "m", result)


def add_plus(count: int, chain: str, result: set[str], concat: bool):
    if count == 0:
        result.add(chain)
    else:
        add_mult(count - 1, chain + "p", result, concat)
        add_plus(count - 1, chain + "p", result, concat)
        if concat:
            add_concat(count - 1, chain + "p", result)


def add_concat(count: int, chain: str, result: set[str]):
    if count == 0:
        result.add(chain)
    else:
        add_mult(count - 1, chain + "c", result, True)
        add_plus(count - 1, chain + "c", result, True)
        add_concat(count - 1, chain + "c", result)


def part2(input):
    """
    >>> part2("190: 10 19\\n190: 10 18")
    190
    """
    total = 0
    for line in input.split("\n"):
        if len(line) == 0:
            continue

        (desired, nums) = parse_line(line)
        combos = build_combos_part2(len(nums) - 1)
        if validate(desired, nums, combos):
            total = total + desired
    return total


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("input").read()
    print("part1:", part1(file))
    print("part2:", part2(file))

import sys


def part1(lines):
    """
    >>> part1([[1, 2, 4]])
    1
    >>> part1([[3, 2, 1]])
    1
    >>> part1([[1, 2, 4], [3, 2, 1], [1, 10, 100]])
    2
    """
    count = 0
    for line in lines:
        nums = [int(x) for x in line.split()]
        if is_safe(nums):
            count = count + 1
    return count


def is_safe(nums):
    if (ascending(nums) or descending(nums)) and differences(nums, 1, 3):
        return True
    return False


def part2(lines):
    """
    >>> part2([1, 10, 2)
    True
    """
    count = 0
    for line in lines:
        nums = [int(x) for x in line.split()]
        for i in range(len(nums)):
            check = nums.copy()
            check.pop(i)
            if is_safe(check):
                count = count + 1
                break
    return count


def ascending(nums):
    """
    >>> ascending([1, 1, 2])
    True
    >>> ascending([1, 2, 1])
    False
    """
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return False
    return True


def descending(nums):
    """
    >>> descending([2, 1, 1])
    True
    >>> descending([1, 2, 1])
    False
    """
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            return False
    return True


def differences(nums, minimum, maximum):
    """
    >>> differences([1, 3, 5], 1, 3)
    True
    >>> differences([1, 5, 1], 1, 3)
    False
    """
    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i - 1])
        if diff < minimum or diff > maximum:
            return False
    return True


if __name__ == "__main__":
    import doctest

    # result = doctest.testmod()
    # if result.failed > 0:
    #     print("exiting...")
    #     sys.exit(1)

    file = open("data/day02/input").readlines()
    print("part1:", part1(file))
    print("part2:", part2(file))

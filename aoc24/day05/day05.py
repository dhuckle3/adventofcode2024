import sys
from collections import defaultdict


def part1(rules: defaultdict(list), updates: list):
    total = 0
    for update in updates:
        total = total + is_valid(rules, update)
    return total


def is_valid(rules, update):
    """
    >>> d = defaultdict(list)
    >>> d[1].append(2)
    >>> is_valid(d, [1,2,3])
    2
    """
    for i, page in enumerate(update[1:], 1):
        for prev_page in update[0:i]:
            if prev_page in rules[page]:
                return 0
    return update[int(len(update) / 2)]


def part2(rules, updates):
    total = 0
    for update in updates:
        if is_valid(rules, update) == 0:
            total = total + fix_update(rules, update)
    return total


def fix_update(rules, update):
    """
    ,>>> d = defaultdict(list)
    .>>> d[1].append(2)
    .>>> d[2].append(3)
    .>>> fix_update(d, [3,1,2])
    .2
    """
    if is_valid(rules, update) != 0:
        return is_valid(rules, update)

    for i, page in enumerate(update[1:], 1):
        for prev_page in update[0:i]:
            if prev_page in rules[page]:
                update.insert(update.index(prev_page), update.pop(update.index(page)))
                return fix_update(rules, update)


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed > 0:
        print("exiting...")
        sys.exit(1)

    file = open("data/day05/input").read()
    [rule_list, updates_list] = file.split("\n\n")

    rules = defaultdict(list)
    for rule in rule_list.split("\n"):
        [a, b] = rule.split("|")
        rules[int(a)].append(int(b))

    updates = []
    for update in updates_list.strip().split("\n"):
        u = [int(u) for u in update.split(",")]
        updates.append(u)

    print("part1:", part1(rules, updates))
    print("part2:", part2(rules, updates))

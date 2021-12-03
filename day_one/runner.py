# -*- coding: utf-8 -*-
"""
Solution for the first day's problem
"""
input_file = list(map(int, open('input.txt').read().splitlines()))


def part_one(data: list):
    """

    :param data:
    :return:
    """
    increases = [y for x, y in enumerate(data[1:]) if data[x] < y]
    return len(increases)


def part_two(data: list):
    """

    :param data:
    :return:
    """
    sliding_sums = [sum(data[i:i + 3]) for i in range(len(data) - 2)]
    return part_one(sliding_sums)


print(part_one(input_file))
print(part_two(input_file))

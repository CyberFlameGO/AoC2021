# -*- coding: utf-8 -*-
"""
Solution for the second day's problem
"""


input_file = open('./input.txt').read()


def part_one(data: str):
    """

    :param data:
    :return:
    """
    horizontal = 0
    depth = 0

    for line in data.strip().split('\n'):
        command, units = line.split(' ')
        units = int(units)

        if command == 'forward':
            horizontal += units
        else:
            depth += units if command == 'down' else -units

    return horizontal * depth


def part_two(data: str):
    """

    :param data:
    :return:
    """
    horizontal = 0
    depth = 0
    aim = 0

    for line in data.strip().split('\n'):
        command, units = line.split(' ')
        units = int(units)

        if command == 'forward':
            horizontal += units
            depth += aim * units
        else:
            aim += units if command == 'down' else -units

    return horizontal * depth


print(part_one(input_file))
print(part_two(input_file))

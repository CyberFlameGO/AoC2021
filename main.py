# -*- coding: utf-8 -*-
"""
Main entrypoint
STALE
"""
global solved_val


def invoke_solution(solution):
    """
    Invoke the solution.
    """
    exec(open(f"./{solution}/runner.py").read())
    return solved_val


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    invoke_solution("day_one")

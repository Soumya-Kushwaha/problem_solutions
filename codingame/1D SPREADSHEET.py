from functools import lru_cache
from operator import *

OPERATORS_MAP = {"VALUE": add, "ADD": add, "SUB": sub, "MULT": mul}

cells = [tuple(input().split()) for _ in range(int(input()))]


def evaluate(arg):
    if arg == "_":
        return 0
    elif arg[0] == "$":
        ref = int(arg[1:])
        return calculate(cells[ref])
    else:
        return int(arg)


@lru_cache(maxsize=128)
def calculate(cell):
    operation, arg_1, arg_2 = cell

    operation = OPERATORS_MAP[operation]
    arg_1 = evaluate(arg_1)
    arg_2 = evaluate(arg_2)

    return operation(arg_1, arg_2)


for cell in cells:
    print(calculate(cell))

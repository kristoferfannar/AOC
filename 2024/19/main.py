import sys
import heapq

if len(sys.argv) != 2:
    exit(1)

file = sys.argv[-1]


def cmb(a, b):
    return (a[0] + b[0], a[1] + b[1])


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


lines = readlines()


def is_possible(stock: list[str], design: str):
    if design == "":
        return True

    for st in stock:
        if len(st) <= len(design) and design[: len(st)] == st:
            found = is_possible(stock, design[len(st) :])
            if found:
                return True
    return False


stock = lines[0].split(", ")

designs = lines[2:]

total = 0
for design in designs:
    if is_possible(stock, design):
        total += 1


print(total)

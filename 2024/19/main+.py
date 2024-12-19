import sys
from functools import cache

if len(sys.argv) != 2:
    exit(1)

file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


@cache
def is_possible(design: str):
    global stock
    if design == "":
        return 1

    total = 0
    for i in range(1, len(design) + 1):
        if design[:i] in stock:
            total += is_possible(design[i:])

    return total


lines = readlines()

stock = set(lines[0].split(", "))
designs = lines[2:]


total = 0
for design in designs:
    total += is_possible(design)

print(total)

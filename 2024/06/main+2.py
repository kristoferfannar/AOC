import sys
from tqdm import tqdm

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines


def comb(one, two) -> tuple[int, ...]:
    """combines two equally sized lists into one"""
    assert len(one) == len(two)

    return tuple([sum(i) for i in zip(one, two)])


lines = readlines()
# the (r, c) tuples for the next step, depending on the direction
next = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C = len(lines[0])
R = len(lines)

dir = 0


start = (-1, -1)
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == "^":
            start = (r, c)

curr = start

trail = set()
while 0 <= curr[0] < R and 0 <= curr[1] < C:
    new = comb(curr, next[dir])

    if not (0 <= new[0] < R and 0 <= new[1] < C):
        break

    if lines[new[0]][new[1]] == "#":
        dir = (dir + 1) % 4
        continue

    curr = new
    trail.add(curr)


blocks = set()
for cell in tqdm(trail):
    clines = [line.copy() for line in lines]
    clines[cell[0]][cell[1]] = "#"

    states = set()
    curr = start

    moves = 0
    dir = 0
    while 0 <= curr[0] < R and 0 <= curr[1] < C:
        clines[curr[0]][curr[1]] = "~"

        # loop found, exit
        if (curr, dir) in states:
            blocks.add(cell)
            break

        states.add((curr, dir))

        new = comb(curr, next[dir])

        if not (0 <= new[0] < R and 0 <= new[1] < C):
            break

        if clines[new[0]][new[1]] == "#":
            dir = (dir + 1) % 4
            continue

        curr = new
        moves += 1

print(len(blocks))

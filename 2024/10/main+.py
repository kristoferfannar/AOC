import sys

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    return [[int(x) for x in line.strip()] for line in lines]


lines = readlines()

R = len(lines) - 1
C = len(lines[0]) - 1

trailheads = []

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == 0:
            trailheads.append((r, c))


def trails(lines, r, c, nines):
    if lines[r][c] == 9:
        if (r, c) not in nines:
            nines[(r, c)] = 0
        nines[(r, c)] += 1
        return nines

    num = lines[r][c]

    if r < R and lines[r + 1][c] == num + 1:
        trails(lines, r + 1, c, nines)

    if r > 0 and lines[r - 1][c] == num + 1:
        trails(lines, r - 1, c, nines)

    if c < C and lines[r][c + 1] == num + 1:
        trails(lines, r, c + 1, nines)

    if c > 0 and lines[r][c - 1] == num + 1:
        trails(lines, r, c - 1, nines)

    return nines


total = 0
for r, c in trailheads:
    nines = trails(lines, r, c, dict())
    total += sum(nines.values())

print(total)

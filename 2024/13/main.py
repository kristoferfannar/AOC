import sys
from time import sleep

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    curr = []
    final = []
    for line in lines:
        if line == "\n":
            final.append(curr)
            curr = []
        else:
            curr.append(line.strip())

    final.append(curr)
    return final


def parsegame(game: list[str]):
    a = game[0][len("Button A: ") :]
    b = game[1][len("Button B: ") :]
    prize = game[2][len("Prize: ") :]

    ax, ay = a.split(", ")
    ax = int(ax[1:])
    ay = int(ay[1:])

    bx, by = b.split(", ")
    bx = int(bx[1:])
    by = int(by[1:])

    px, py = prize.split(", ")
    px = int(px[2:])
    py = int(py[2:])

    return ax, ay, bx, by, px, py


def ratio(ax, ay, bx, by, x, y):
    ar, br = 1, 1

    inc_a = ax / ay > bx / by

    while (r := (ar * ax + br * bx) / (ar * ay + br * by)) != (x / y):

        # no ratio found
        if (ar * ax + br * bx) > x or (ar * ay + br * by) > y:
            return -1, -1

        if r > x / y:
            if inc_a:
                br += 1
            else:
                ar += 1

        elif r < x / y:
            if inc_a:
                ar += 1
            else:
                br += 1

    return ar, br


games = readlines()


total = 0
for game in games:
    ax, ay, bx, by, x, y = parsegame(game)
    ar, br = ratio(ax, ay, bx, by, x, y)

    if -1 in [ar, br]:
        continue

    mult = x // (ar * ax + br * bx)
    total += mult * ar * 3 + mult * br * 1
    # print(f"{(mult * ar, mult * br)}")
    # print(f"A: {(ax, ay)}, B: {(bx, by)}, {(ar, br)}, Prize: {(x, y)}")

print(total)

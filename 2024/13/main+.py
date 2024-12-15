import sys

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
    px = int(px[2:]) + 10000000000000
    py = int(py[2:]) + 10000000000000

    return ax, ay, bx, by, px, py


games = readlines()

total = 0
for game in games:
    ax, ay, bx, by, x, y = parsegame(game)

    # math hints from https://www.youtube.com/watch?v=-5J-DAsWuJc
    # i should have caught that without help but I'm in finals so I gave up..
    i = (x * by - y * bx) / (ax * by - ay * bx)
    j = (x * ay - y * ax) / (bx * ay - by * ax)

    if not (i == int(i) and j == int(j)):
        continue

    i = int(i)
    j = int(j)

    total += 3 * i + j

print(total)

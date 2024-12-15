import sys

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    return lines


lines = readlines()


box = []
moves = ""

crossed = False
for line in lines:
    if line == "\n":
        crossed = True
    elif not crossed:
        box.append(list(line.strip()))
    else:
        moves += line.strip()

R = len(box)
C = len(box[0])

pos = [-1, -1]


for r in range(R):
    for c in range(C):
        if box[r][c] == "@":
            pos = [r, c]
            break

dirs = "^>v<"
nexts = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def cmb(curr, next):
    return (curr[0] + next[0], curr[1] + next[1])


def move(box, pos, dir):
    didx = dirs.index(dir)
    next = cmb(pos, nexts[didx])

    if box[next[0]][next[1]] == "#":
        return

    if box[next[0]][next[1]] == ".":
        box[pos[0]][pos[1]] = "."
        pos[0] = next[0]
        pos[1] = next[1]
        box[pos[0]][pos[1]] = "@"
        return

    curr = next
    pushed = False
    while box[curr[0]][curr[1]] != "#":
        if box[curr[0]][curr[1]] == ".":
            box[curr[0]][curr[1]] = "O"
            pushed = True
            break

        curr = cmb(curr, nexts[didx])

    if pushed:
        box[pos[0]][pos[1]] = "."
        pos[0] = next[0]
        pos[1] = next[1]
        box[pos[0]][pos[1]] = "@"


def gps(box):
    total = 0
    for r in range(R):
        for c in range(C):
            if box[r][c] == "O":
                total += 100 * r + c

    return total


for dir in moves:
    move(box, pos, dir)

print(gps(box))

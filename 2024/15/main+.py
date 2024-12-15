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


def boxify(line):
    new = ""
    for char in line:
        if char in "#.":
            new += char * 2
        elif char == "O":
            new += "[]"
        else:
            new += "@."

    return list(new)


crossed = False
for line in lines:
    if line == "\n":
        crossed = True
    elif not crossed:
        box.append(boxify(line.strip()))
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


def shiftbox(box, pos, dir):
    """for vertically shifting boxes"""
    r, c = pos

    didx = dirs.index(dir)
    d = nexts[didx]
    nr, _ = cmb(pos, d)

    if box[nr][c] == "#" or box[nr][c + 1] == "#":
        return False

    if box[nr][c] == "[":
        shift = shiftbox(box, (nr, c), dir)
        if not shift:
            return False

    elif box[nr][c] == "]" and box[nr][c + 1] == "[":
        shift = shiftbox(box, (nr, c - 1), dir) and shiftbox(box, (nr, c + 1), dir)
        if not shift:
            return False

    elif box[nr][c] == "]":
        shift = shiftbox(box, (nr, c - 1), dir)
        if not shift:
            return False

    elif box[nr][c + 1] == "[":
        shift = shiftbox(box, (nr, c + 1), dir)
        if not shift:
            return False

    if box[nr][c] == "." and box[nr][c + 1] == ".":
        box[nr][c] = "["
        box[nr][c + 1] = "]"

        box[r][c] = "."
        box[r][c + 1] = "."
        return True


def shift(box, start, end, dir):
    assert box[end[0]][end[1]] == "."

    if dir in "^v":
        didx = dirs.index(dir)
        nr, nc = cmb(start, nexts[didx])

        cbox = [b.copy() for b in box]

        if box[nr][nc] == "[":
            success = shiftbox(cbox, (nr, nc), dir)
        elif box[nr][nc] == "]":
            success = shiftbox(cbox, (nr, nc - 1), dir)
        else:
            raise Exception("hmmm")

        if success:
            for r in range(R):
                for c in range(C):
                    box[r][c] = cbox[r][c]
            box[nr][nc] = "@"
        return success

    elif dir == "<":
        r = start[0]
        for i in range(end[1], start[1]):
            box[r][i] = box[r][i + 1]

    elif dir == ">":
        r = start[0]
        for i in range(end[1], start[1], -1):
            box[r][i] = box[r][i - 1]

    return True


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
    shifted = False
    while box[curr[0]][curr[1]] != "#":
        if box[curr[0]][curr[1]] == ".":
            shifted = shift(box, pos, curr, dir)
            break

        curr = cmb(curr, nexts[didx])

    if shifted:
        box[pos[0]][pos[1]] = "."
        pos[0] = next[0]
        pos[1] = next[1]


def gps(box):
    total = 0
    for r in range(R):
        for c in range(C):
            if box[r][c] == "[":
                total += 100 * r + c

    return total


for dir in moves:
    move(box, pos, dir)

print(gps(box))

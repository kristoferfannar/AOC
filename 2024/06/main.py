import sys
from time import sleep
import tqdm

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = [list(line.strip()) for line in f.readlines()]

    return lines


lines = readlines()


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# the (r, c) tuples for the next step, depending on the direction
next = [(-1, 0), (0, 1), (1, 0), (0, -1)]


C = len(lines[0])
R = len(lines)
columns = [[] for _ in range(C)]
rows = [[] for _ in range(R)]
pos = (-1, -1)

dir = -1
DIRS = "^>v<"


def comb(one, two):
    """combines two equally sized lists into one"""
    assert len(one) == len(two)

    return [sum(i) for i in zip(one, two)]


def is_stuck(lines, pos, dir):
    return (
        dir == UP
        and pos[0] == 0
        or dir == DOWN
        and pos[0] == R - 1
        or dir == LEFT
        and pos[1] == 0
        or dir == RIGHT
        and pos[1] == C - 1
    )
    # next_dir = (dir + 1) % 4
    # next_r, next_c = comb(pos, next[next_dir])
    # if not (0 <= next_r < R and 0 <= next_c < C):
    #     return True
    #
    # return lines[next_r][next_c] == "#"


seen: set[tuple[int, int]] = set()


def move(lines, from_, to: tuple[int, int], dir):
    total = 0

    # print(f"from-{from_} to-{to}")
    # print(f"seen {seen}")

    if dir % 2 == 0:
        for r in range(min(from_[0], to[0]), max(from_[0], to[0]) + 1):
            if (r, to[1]) not in seen:
                total += 1
                lines[r][to[1]] = "x"
                seen.add((r, to[1]))

        # print(f"r: {min(from_[0], to[0])} to {max(from_[0], to[0])}")
        # print(f"seen - after {seen}")
        # print(f"moved {abs(from_[0] - to[0])} steps, {total} new")
    else:
        for c in range(min(from_[1], to[1]), max(from_[1], to[1]) + 1):
            if (to[0], c) not in seen:
                total += 1
                lines[to[0]][c] = "x"
                seen.add((to[0], c))

        # print(f"c: {min(from_[1], to[1])} to {max(from_[1], to[1])}")
        # print(f"seen - after {seen}")
        # print(f"moved {abs(from_[1] - to[1])} steps, {total} new")

    # print(f"{len(seen)} in seen - {seen}")
    # print(f"{total} new")

    return total


def find_to(rows: list[list], cols: list[list], pos, dir):
    r, c = pos

    # left or right
    if dir % 2 == 1:
        inc = int(dir == RIGHT)
        next_col_idx = R - 1 if inc else 0
        for col_idx in rows[r][:: inc * 2 - 1]:
            if dir == LEFT and col_idx < c:
                return (r, col_idx + 1)

            if dir == RIGHT and col_idx > c:
                return (r, col_idx - 1)

        return (r, next_col_idx)
    else:  # up or down
        inc = int(dir == DOWN)
        next_row_idx = C - 1 if inc else 0
        for row_idx in cols[c][:: inc * 2 - 1]:
            if dir == UP and row_idx < r:
                return (row_idx + 1, c)

            if dir == DOWN and row_idx > r:
                return (row_idx - 1, c)

        return (next_row_idx, c)


for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            columns[c].append(r)
            rows[r].append(c)

        if char in DIRS:
            pos = (r, c)
            dir = DIRS.index(char)

            # print(f"at {pos}, going: {dir} ")
            seen.add(pos)


total = 1

# we'll turn into the starting direction
dir = (dir - 1) % 4
dirnames = ["up", "right", "down", "left"]


def dbg(lines, pos):
    for r in range(R):
        for c in range(C):
            if pos == (r, c):
                print("@", end="")
            else:
                print(lines[r][c], end="")

        print()


stopped = set()

# print(f"R-{R} C-{C}")

turns = 0
while not is_stuck(lines, pos, dir) and not (pos, dir) in stopped:
    turns += 1
    stopped.add((pos, dir))
    dir = (dir + 1) % 4
    to = find_to(rows, columns, pos, dir)
    total += move(lines, pos, to, dir)

    # print(f"going {dirnames[dir]}, from {pos} to {to}")
    pos = to
    # dbg(lines, pos)
    # input("press enter")
    # sleep(0.1)

print(f"turns: {turns}")

print(f"total: {total}")

import sys

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
dirnames = ["up", "right", "down", "left"]
# the (r, c) tuples for the next step, depending on the direction
next = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C = len(lines[0])
R = len(lines)
columns = [[] for _ in range(C)]
rows = [[] for _ in range(R)]
pos = (-1, -1)
dir = -1
DIRS = "^>v<"
SEEN: set[tuple[int, int]] = set()
found: set[tuple[int, int]] = set()
stopped = set()


for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            columns[c].append(r)
            rows[r].append(c)

        if char in DIRS:
            pos = (r, c)
            dir = DIRS.index(char)

            SEEN.add(pos)


# we'll turn into the starting direction
dir = (dir - 1) % 4


def comb(one, two) -> tuple[int, ...]:
    """combines two equally sized lists into one"""
    assert len(one) == len(two)

    return tuple([sum(i) for i in zip(one, two)])


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


def loops(lines, lseen, lstopped, pos, dir):
    """Basically rerun the original simulation but with a turn"""
    if is_stuck(lines, pos, dir):
        return False

    crows = [row.copy() for row in rows]
    ccols = [col.copy() for col in columns]

    block = (pos[0] + next[dir][0], pos[1] + next[dir][1])

    lines[block[0]][block[1]] = "O"
    crows[block[0]].append(block[1])
    ccols[block[1]].append(block[0])
    crows[block[0]].sort()
    ccols[block[1]].sort()

    while not is_stuck(lines, pos, dir) and not (pos, dir) in lstopped:
        lstopped.add((pos, dir))
        dir = (dir + 1) % 4
        to = find_to(crows, ccols, pos, dir)
        move(lines, lseen, pos, to, dir, looped=True)
        pos = to

    return (pos, dir) in lstopped


def move(lines, seen, from_, to: tuple[int, int], dir, looped=False):
    # we're already there
    if from_ == to:
        return 0

    if dir % 2 == 0:
        inv = (to[0] - from_[0]) // abs(to[0] - from_[0])
        for r in range(from_[0], to[0] + inv, inv):
            if looped:
                lines[r][to[1]] = ":"
            else:
                lines[r][to[1]] = "x"
            if (r, to[1]) not in seen:
                seen.add((r, to[1]))

            # see if we would loop if we were to turn right here
            if not looped and r != to[0]:
                clines = [line.copy() for line in lines]
                if loops(
                    clines,
                    seen.copy(),
                    set(),
                    (r, to[1]),
                    dir,
                ):
                    block = comb((r, to[1]), next[dir])
                    print(f"looped at {block}")
                    assert isinstance(block, tuple) and len(block) == 2
                    found.add(block)

            # dbg(lines, pos)
            # input("press enter")

    else:
        inv = (to[1] - from_[1]) // abs(to[1] - from_[1])

        for c in range(from_[1], to[1] + inv, inv):
            if looped:
                lines[to[0]][c] = ":"
            else:
                lines[to[0]][c] = "x"
            if (to[0], c) not in seen:
                seen.add((to[0], c))

            # see if we would loop if we were to turn right here
            if not looped and c != to[1]:
                clines = [line.copy() for line in lines]
                if loops(
                    clines,
                    seen.copy(),
                    set(),
                    (to[0], c),
                    dir,
                ):
                    block = comb((to[0], c), next[dir])
                    print(f"looped at {block}")
                    assert isinstance(block, tuple) and len(block) == 2
                    found.add(block)

            # dbg(lines, pos)
            # input("press enter")

    return


def find_to(rows: list[list], cols: list[list], pos, dir):
    r, c = pos

    # left or right
    if dir % 2 == 1:
        inc = int(dir == RIGHT)
        next_col_idx = C - 1 if inc else 0
        for col_idx in rows[r][:: inc * 2 - 1]:
            if dir == LEFT and col_idx < c:
                return (r, col_idx + 1)

            if dir == RIGHT and col_idx > c:
                return (r, col_idx - 1)

        return (r, next_col_idx)
    else:  # up or down
        inc = int(dir == DOWN)
        next_row_idx = R - 1 if inc else 0
        for row_idx in cols[c][:: inc * 2 - 1]:
            if dir == UP and row_idx < r:
                return (row_idx + 1, c)

            if dir == DOWN and row_idx > r:
                return (row_idx - 1, c)

        return (next_row_idx, c)


def dbg(lines, pos):
    for r in range(R):
        for c in range(C):
            if pos == (r, c):
                print("@", end="")
            else:
                print(lines[r][c], end="")

        print()


while not is_stuck(lines, pos, dir) and not (pos, dir) in stopped:
    stopped.add((pos, dir))
    dir = (dir + 1) % 4
    to = find_to(rows, columns, pos, dir)

    move(lines, SEEN, pos, to, dir)

    pos = to

print(f"total: {len(found)}")

# 2134 too high
# 2089 too high
# 2056 too high

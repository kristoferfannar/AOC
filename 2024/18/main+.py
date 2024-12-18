import sys
import heapq

if len(sys.argv) != 2:
    exit(1)

file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def cmb(a, b):
    return (a[0] + b[0], a[1] + b[1])


def traverse(grid, start, end):
    frontier: list[tuple[int, tuple[int, int]]] = [(0, start)]
    seen = set()

    while frontier:
        cost, pos = heapq.heappop(frontier)

        # we've already been here for cheaper
        if pos in seen:
            continue

        seen.add(pos)

        if pos == end:
            return cost

        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new = cmb(pos, dir)

            if (
                not (0 <= new[0] < R)
                or not (0 <= new[1] < C)
                or not (grid[new[0]][new[1]] == ".")
                or new in seen
            ):
                continue

            heapq.heappush(frontier, (cost + 1, new))

    return 0


lines = readlines()
# R = 7
# C = 7
# BYTES = 12
R = 71
C = 71
BYTES = 1024
nums = []

l = 0
h = len(lines) - 1
while l + 1 < h:
    m = (l + h) // 2
    grid = [["."] * C for _ in range(R)]
    for line in lines[: m + 1]:
        c, r = map(int, line.split(","))
        nums.append((r, c))
        grid[r][c] = "#"

    traversed = traverse(grid, (0, 0), (R - 1, C - 1))

    if traversed:
        l = m
    else:
        h = m

print(f"{lines[h]}")

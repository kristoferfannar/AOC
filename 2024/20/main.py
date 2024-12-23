import sys
import heapq
from collections import defaultdict

if len(sys.argv) != 2:
    exit(1)
file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]


def cmb(a, b):
    return (a[0] + b[0], a[1] + b[1])


lines = readlines()

R = len(lines)
C = len(lines[0])

start = (0, 0)
end = (0, 0)

for r in range(R):
    for c in range(C):
        if lines[r][c] == "S":
            start = (r, c)
            lines[r][c] = "."
        if lines[r][c] == "E":
            end = (r, c)
            lines[r][c] = "."


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def adjs(pos):
    return [cmb(pos, dir) for dir in dirs]


def find(grid, start, target, cheated=False, seen=None):
    scores = defaultdict(lambda: 0)
    if not seen:
        seen = set()
    frontier: list[tuple[int, tuple[int, int]]] = [(0, start)]

    while frontier:
        cost, pos = heapq.heappop(frontier)
        seen.add(pos)

        if pos == target:
            scores[cost] += 1

        for dir in adjs(pos):
            if dir in seen:
                continue
            if not (0 <= dir[0] < R and 0 <= dir[1] < C):
                continue
            if grid[dir[0]][dir[1]] == "#":
                continue

            heapq.heappush(frontier, (cost + 1, dir))

        if not cheated:
            for cheat in adjs(pos):
                cheatscores = find(grid, cheat, target, cheated=True, seen=seen.copy())
                for ccost, cnum in cheatscores.items():
                    scores[ccost + cost + 1] += cnum

    return scores


clines = [line.copy() for line in lines]
org = find(clines, start, end, cheated=True)  # no cheats == no cheats left
org = list(org.keys())[0]

clines = [line.copy() for line in lines]
scores = find(clines, start, end)

total = 0
for score, num in sorted(scores.items(), key=lambda x: x[0], reverse=True):
    if org - score >= 100:
        total += num

print(total)

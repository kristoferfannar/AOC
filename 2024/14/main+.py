import sys
import re

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


lines = readlines()


R = 103
C = 101

pos = dict()

coords = []

for line in lines:
    px, py, vx, vy = list(map(int, re.findall("-?\d+", line)))
    coords.append([px, py, vx, vy])

for sec in range(R * C):
    grid = [[0] * C for _ in range(R)]
    for px, py, vx, vy in coords:

        endx = (px + sec * vx) % C
        endy = (py + sec * vy) % R

        grid[endy][endx] += 1

    success = False
    for r in range(R):
        if success:
            break
        count = 0
        for c in range(C):
            if count > 10:
                success = True
                break
            if grid[r][c] == 1:
                count += 1
            else:
                count = 0

    if success:
        break

# for r in range(R):
#     for c in range(C):
#         if grid[r][c] > 0:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

print(sec)

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

SEC = 100
pos = dict()
quads = [0] * 4
for line in lines:
    px, py, vx, vy = list(map(int, re.findall("-?\d+", line)))

    endx = (px + SEC * vx) % C
    endy = (py + SEC * vy) % R

    if endx < C // 2 and endy < R // 2:
        quads[0] += 1
    elif endx < C // 2 and endy > R // 2:
        quads[1] += 1
    elif endx > C // 2 and endy < R // 2:
        quads[2] += 1
    elif endx > C // 2 and endy > R // 2:
        quads[3] += 1

    if (endx, endy) not in pos:
        pos[(endx, endy)] = 0
    pos[(endx, endy)] += 1

# for r in range(R):
#     for c in range(C):
#         if c == C // 2 or r == R // 2:
#             print(" ", end="")
#         elif (c, r) not in pos:
#             print(".", end="")
#         else:
#             print(pos[(c, r)], end="")
#     print()

print(quads[0] * quads[1] * quads[2] * quads[3])

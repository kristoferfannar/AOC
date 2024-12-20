import sys
import re

if len(sys.argv) != 2:
    exit(1)

file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return lines


lines = readlines()

p1 = 0
p2 = 0
for line in lines:
    l, w, h = map(int, re.findall("\d+", line))
    p1 += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
    p2 += min(l + w, w + h, h + l) * 2 + l * w * h

print(p1)
print(p2)

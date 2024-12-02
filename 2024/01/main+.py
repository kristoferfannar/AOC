import heapq
from collections import Counter


def readlines():
    lines = []
    with open("input.txt", "r") as file:
        lines = [[int(x) for x in n.strip().split()] for n in file.readlines()]
    return lines


lines = readlines()


ls = []
rs = []

for l, r in lines:
    ls.append(l)
    rs.append(r)

rc = Counter(rs)

diff = 0
while ls:
    lcurr = heapq.heappop(ls)
    if lcurr in rc:
        diff += lcurr * rc[lcurr]

print(diff)

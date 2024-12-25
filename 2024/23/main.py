import sys
from collections import defaultdict

if len(sys.argv) != 2:
    exit()

file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def cycles(node, network, l=0, seen=None, start=None, traversal=None):
    if not traversal:
        traversal = []

    if not start:
        start = node

    if not seen:
        seen = set()

    cycl = set()
    if l > 3:
        return cycl

    if l == 3 and node == start:
        return set([tuple(sorted(traversal))])

    for neighbor in network[node]:
        c = cycles(neighbor, network, l + 1, seen.copy(), start, [*traversal, neighbor])
        cycl = cycl.union(c)

    return cycl


lines = readlines()

conns = defaultdict(lambda: [])

for line in lines:
    a, b = line.split("-")
    conns[a].append(b)
    conns[b].append(a)


allcycles = set()
for conn in [c for c in conns.keys() if c[0] == "t"]:
    c = cycles(conn, conns)
    allcycles = allcycles.union(c)

print(len(allcycles))

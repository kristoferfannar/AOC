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


bestever = 0


def clique(node: str, cliq: set) -> set:
    global conns
    global bestever

    best = cliq

    for neighbor in conns[node]:
        if cliq.issubset(conns[neighbor]):
            ccliq = cliq.copy()
            ccliq.add(neighbor)
            curr = clique(neighbor, ccliq)

            if len(curr) > len(best):
                best = curr

            if len(curr) > bestever:
                bestever = len(curr)
                print(f"found better {bestever}")
                print(",".join(sorted(curr)))

    return best


# maximal clique from https://www.geeksforgeeks.org/maximal-clique-problem-recursive-solution/
# not optimized, NP version
def maxClique():
    global conns
    best = set()

    count = 0
    for node in conns.keys():
        print(round(count * 100 / len(conns), 2), "%", sep="")
        count += 1
        curr = clique(node, set())

        if len(curr) > len(best):
            best = curr

    return best


# optimized clique from https://www.altcademy.com/blog/compute-the-maximum-clique-in-a-graph/
# somehow it's instant
def bron_kerbosch(r, p, x, network):
    rs = [r]
    if not p and not x:
        return rs

    for node in p.copy():
        newrs = bron_kerbosch(r | {node}, p & network[node], x & network[node], network)
        rs.extend(newrs)
        p.remove(node)
        x.add(node)

    return rs


lines = readlines()
conns = defaultdict(lambda: set())

for line in lines:
    a, b = line.split("-")
    conns[a].add(b)
    conns[b].add(a)

cliques = bron_kerbosch(set(), set(conns.keys()), set(), conns)
best = max(cliques, key=lambda x: len(x))

print(",".join(sorted(best)))

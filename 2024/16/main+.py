import sys
import heapq

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


R = len(lines)
C = len(lines[0])

start = (0, 0)
end = (0, 0)

dirs = "^>v<"
nexts = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def cmb(a, b):
    return (a[0] + b[0], a[1] + b[1])


def isin(frontier, pos, dir):
    for _, p, d, _ in frontier:
        if p == pos and d == dir:
            return True

    return False


def decrease(frontier, state):
    for i in range(len(frontier)):
        if frontier[i][1] == state[1] and frontier[i][2] == state[2]:
            if frontier[i][0] == state[0]:
                frontier[i][3] = frontier[i][3].union(state[3])
            else:
                frontier[i][3] = state[3]

            frontier[i][0] = min(frontier[i][0], state[0])
            heapq.heapify(frontier)


def astar(start, target):
    paths = 0
    besttiles = set()
    best = float("inf")
    dir = 1  # east
    frontier = [[0 + h(start, target), start, dir, set([start])]]
    explored = set()

    while frontier:
        cost, pos, dir, tiles = heapq.heappop(frontier)
        explored.add(pos)

        if cost > best:
            break

        if lines[pos[0]][pos[1]] == "#":
            print(f"I'm at {pos}")
            raise Exception()

        if pos == target:
            paths += 1
            best = cost
            besttiles = besttiles.union(tiles)

        for nextdir, n in enumerate(nexts):
            next = cmb(pos, n)
            if lines[next[0]][next[1]] == "#":
                continue

            if isin(frontier, next, nextdir) and next in explored:
                continue

            nextcost = 1 + cost - h(pos, target) + h(next, target)

            if abs(nextdir - dir) == 1 or abs(nextdir - dir) == 3:
                nextcost += 1000

            if abs(nextdir - dir) == 2:
                nextcost += 2000

            nexttiles = tiles.copy()
            nexttiles.add(next)
            nextstate = [nextcost, next, nextdir, nexttiles]
            if isin(frontier, next, nextdir):
                decrease(frontier, nextstate)
            else:
                heapq.heappush(frontier, nextstate)

    return len(besttiles)


def h(start, end):
    cost = abs(start[0] - end[0]) + abs(start[1] - end[1])

    return cost


for r in range(R):
    for c in range(C):
        if lines[r][c] == "E":
            end = (r, c)
        elif lines[r][c] == "S":
            start = (r, c)


print(astar(start, end))

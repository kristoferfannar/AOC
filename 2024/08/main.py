import sys

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    return [list(line.strip()) for line in lines]


lines = readlines()

R = len(lines)
C = len(lines[0])

antennas: dict[str, list] = dict()


for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] != ".":
            if lines[r][c] not in antennas:
                antennas[lines[r][c]] = []

            antennas[lines[r][c]].append((r, c))


antinodes: set[tuple[int, int]] = set()


def get_new(a, b):
    rdiff = abs(a[0] - b[0])
    cdiff = abs(a[1] - b[1])

    inv = (a[0] - b[0]) * (a[1] - b[1]) < 0

    if a[0] > b[0]:
        hi = a
        lo = b
    else:
        hi = b
        lo = a

    r1 = hi[0] + rdiff
    c1 = hi[1] + cdiff

    r2 = lo[0] - rdiff
    c2 = lo[1] - cdiff

    if inv:
        c1 -= 2 * cdiff
        c2 += 2 * cdiff

    return [(r1, c1), (r2, c2)]


for ant, locs in antennas.items():
    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            l1, l2 = locs[i], locs[j]
            n1, n2 = get_new(l1, l2)

            if 0 <= n1[0] < R and 0 <= n1[1] < C:
                antinodes.add(n1)

            if 0 <= n2[0] < R and 0 <= n2[1] < C:
                antinodes.add(n2)

print(len(antinodes))

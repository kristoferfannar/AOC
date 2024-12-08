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
    rdiff = a[0] - b[0]
    cdiff = a[1] - b[1]

    if rdiff < 0:
        rdiff *= -1
        cdiff *= -1

    rcurr = a[0] % rdiff
    jumps = a[0] // rdiff
    ccurr = a[1] - cdiff * jumps

    final = []

    while rcurr < R:
        if 0 <= rcurr < R and 0 <= ccurr < C:
            final.append((rcurr, ccurr))
        rcurr += rdiff
        ccurr += cdiff

    return final


for ant, locs in antennas.items():
    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            l1, l2 = locs[i], locs[j]
            news = get_new(l1, l2)

            for new in news:
                if 0 <= new[0] < R and 0 <= new[1] < C:
                    antinodes.add(new)

print(len(antinodes))

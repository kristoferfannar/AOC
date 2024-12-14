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

R = len(lines) - 1
C = len(lines[0]) - 1


def find_plot(r, c, plot=set()):
    if (r, c) in plot:
        return plot
    plot.add((r, c))

    char = lines[r][c]
    if r < R and lines[r + 1][c] == char:
        find_plot(r + 1, c, plot)

    if r > 0 and lines[r - 1][c] == char:
        find_plot(r - 1, c, plot)

    if c < C and lines[r][c + 1] == char:
        find_plot(r, c + 1, plot)

    if c > 0 and lines[r][c - 1] == char:
        find_plot(r, c - 1, plot)

    return plot


def perimeter(plots):
    per = 0

    for r, c in plots:
        if r == R or (r + 1, c) not in plots:
            per += 1
        if r == 0 or (r - 1, c) not in plots:
            per += 1
        if c == C or (r, c + 1) not in plots:
            per += 1
        if c == 0 or (r, c - 1) not in plots:
            per += 1

    return per


areas = dict()
seen = set()
for r in range(R + 1):
    for c in range(C + 1):
        if lines[r][c] not in areas:
            areas[lines[r][c]] = []

        if (r, c) not in seen:
            plot = find_plot(r, c, set())
            seen = seen.union(plot)
            areas[lines[r][c]].append(plot)


total = 0
for letter, plots in areas.items():
    for plot in plots:
        per = perimeter(plot)
        total += len(plot) * per

print(total)

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


def find_plot(r, c, plot=set()):
    if (r, c) in plot:
        return plot
    plot.add((r, c))

    char = lines[r][c]
    if r < R - 1 and lines[r + 1][c] == char:
        find_plot(r + 1, c, plot)

    if r > 0 and lines[r - 1][c] == char:
        find_plot(r - 1, c, plot)

    if c < C - 1 and lines[r][c + 1] == char:
        find_plot(r, c + 1, plot)

    if c > 0 and lines[r][c - 1] == char:
        find_plot(r, c - 1, plot)

    return plot


UP = 1
DOWN = 2
LEFT = 4
RIGHT = 8


def sides(plots: set):
    total = 0
    while plots:
        r, c = plots.pop()

        char = lines[r][c]

        # is upper left corner
        if (r == 0 or lines[r - 1][c] != char) and (c == 0 or lines[r][c - 1] != char):
            total += 1

        # is upper right corner
        if (r == 0 or lines[r - 1][c] != char) and (
            c == C - 1 or lines[r][c + 1] != char
        ):
            total += 1

        # is lower left corner
        if (r == R - 1 or lines[r + 1][c] != char) and (
            c == 0 or lines[r][c - 1] != char
        ):
            total += 1

        # is lower right corner
        if (r == R - 1 or lines[r + 1][c] != char) and (
            c == C - 1 or lines[r][c + 1] != char
        ):
            total += 1

        # is inner upper left corner
        if (
            r > 0
            and c > 0
            and lines[r - 1][c] == char
            and lines[r][c - 1] == char
            and lines[r - 1][c - 1] != char
        ):
            total += 1

        # is inner upper right corner
        if (
            r > 0
            and c < C - 1
            and lines[r - 1][c] == char
            and lines[r][c + 1] == char
            and lines[r - 1][c + 1] != char
        ):
            total += 1

        # is inner lower left corner
        if (
            r < R - 1
            and c > 0
            and lines[r + 1][c] == char
            and lines[r][c - 1] == char
            and lines[r + 1][c - 1] != char
        ):
            total += 1

        # is inner lower right corner
        if (
            r < R - 1
            and c < C - 1
            and lines[r + 1][c] == char
            and lines[r][c + 1] == char
            and lines[r + 1][c + 1] != char
        ):
            total += 1

    return total


areas = dict()
seen = set()
for r in range(R):
    for c in range(C):
        if lines[r][c] not in areas:
            areas[lines[r][c]] = []

        if (r, c) not in seen:
            plot = find_plot(r, c, set())
            seen = seen.union(plot)
            areas[lines[r][c]].append(plot)


total = 0
for letter, plots in areas.items():
    for plot in plots:
        l = len(plot)
        per = sides(plot)
        total += l * per

print(f"{total}")

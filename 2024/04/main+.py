def readlines():
    lines = []
    with open("in.txt") as f:
        lines = f.readlines()
    return lines


lines = readlines()


def find_xmas(lines, x, y):
    if lines[y][x] != "A":
        return 0

    if (
        lines[y + 1][x - 1] != lines[y - 1][x + 1]
        and lines[y + 1][x - 1] in "MS"
        and lines[y - 1][x + 1] in "MS"
        and lines[y + 1][x + 1] != lines[y - 1][x - 1]
        and lines[y + 1][x + 1] in "MS"
        and lines[y - 1][x - 1] in "MS"
    ):
        return 1

    return 0


xmas = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        xmas += find_xmas(lines, x, y)

print(xmas)

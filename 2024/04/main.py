def readlines():
    lines = []
    with open("in.txt") as f:
        lines = f.readlines()
    return lines


lines = readlines()


def find_xmas(lines, x, y):
    if lines[y][x] != "X":
        return 0

    dirs = [(1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1)]
    word = "XMAS"

    exists = [1] * len(dirs)

    for i in range(len(word)):
        for j in range(len(dirs)):
            if exists[j]:
                nx = x + i * dirs[j][0]
                ny = y + i * dirs[j][1]
                if ny >= len(lines) or nx >= len(lines[0]) or nx < 0 or ny < 0:
                    exists[j] = 0
                    continue

                if lines[ny][nx] != word[i]:
                    exists[j] = 0

    return sum(exists)


xmas = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        xmas += find_xmas(lines, x, y)

print(xmas)

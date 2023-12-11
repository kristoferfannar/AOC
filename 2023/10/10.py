from time import sleep
DOWN = "|LJ"
LEFT = "-LF"
RIGHT = "-J7"
UP = "|F7"

DIRECTIONS = {"S": (UP, DOWN, LEFT, RIGHT), "F": (DOWN, RIGHT), "L": (UP, RIGHT), "7": (
    DOWN, LEFT), "J": (UP, LEFT), "-": (LEFT, RIGHT), "|": (UP, DOWN)}


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def dimensions(lines):
    return len(lines[0]), len(lines)


def findS(lines: list[str]):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y)
    raise Exception("S not found")


def createClone(length, width):
    return [[(".", -1) for _ in range(width)] for y in range(length)]


def getUncheckedNeighbours(lines: list[str], clone: list[list[str]], x: int, y: int):
    up = lines[y - 1][x] if y > 0 and clone[y - 1][x][0] == "." else None
    down = lines[y + 1][x] if y < len(lines) - \
        1 and clone[y + 1][x][0] == "." else None
    left = lines[y][x - 1] if x > 0 and clone[y][x - 1][0] == "." else None
    right = lines[y][x + 1] if x < len(lines[0]) - \
        1 and clone[y][x + 1][0] == "." else None

    return up, down, left, right


def markPipes(lines: list[str], clone: list[list[str]], validUnchecked: list):
    validUncheckedCount = len(validUnchecked)

    furthestDistance = 0

    while validUncheckedCount > 0:
        x, y, dist = validUnchecked.pop(0)
        if dist > furthestDistance:
            #     print(furthestDistance, x, y)
            furthestDistance = dist

        pipe = lines[y][x]
        clone[y][x] = (pipe, dist)

        up, down, left, right = getUncheckedNeighbours(lines, clone, x, y)

        for dir in DIRECTIONS[pipe]:
            if dir == UP and up != None and up in UP:
                # markPipes(lines, clone)
                validUnchecked.append((x, y - 1, dist + 1))

            elif dir == DOWN and down != None and down in DOWN:
                # markPipes(lines, clone)
                validUnchecked.append((x, y + 1, dist + 1))

            elif dir == LEFT and left != None and left in LEFT:
                # markPipes(lines, clone)
                validUnchecked.append((x - 1, y, dist + 1))

            elif dir == RIGHT and right != None and right in RIGHT:
                # markPipes(lines, clone)
                validUnchecked.append((x + 1, y, dist + 1))

        validUncheckedCount = len(validUnchecked)

    return furthestDistance


lines = loadFile("input.txt")
length, width = dimensions(lines)

clone = createClone(length, width)
sX, sY = findS(lines)


validUnchecked = [(sX, sY, 0)]

furthestDistance = markPipes(lines, clone, validUnchecked)

print(furthestDistance)

# for line in lines:
#     print(line)

# print()

for c in clone:
    print("".join([x[0] for x in c]))

# with open("input+.txt", "w") as file:
#     for c in clone:
#         file.write("".join([x[0] for x in c]))
#         file.write("\n")

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
    return len(lines), len(lines[0])


def findS(lines: list[str]):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y)
    raise Exception("S not found")


def createClone(height, width):
    return [[(".", -1) for _ in range(width)] for y in range(height)]


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


def getNeighbours(lines: list[list[str]], x: int, y: int):
    up = lines[y - 1][x][0] if y > 0 else None
    down = lines[y + 1][x][0] if y < len(lines[0]) - 1 else None
    left = lines[y][x - 1][0] if x > 0 else None
    right = lines[y][x + 1][0] if x < len(lines) - 1 else None

    return up, down, left, right


def changeS(lines: list[list[str]], sX: int, sY: int):
    up, down, left, right = getNeighbours(lines, sX, sY)

    if up and up in UP and down and down in DOWN:
        lines[sY][sX] = ("|", 0)
    elif up and up in UP and left and left in LEFT:
        lines[sY][sX] = ("J", 0)
    elif up and up in UP and right and right in RIGHT:
        lines[sY][sX] = ("L", 0)
    elif down and down in DOWN and left and left in LEFT:
        lines[sY][sX] = ("7", 0)
    elif down and down in DOWN and right and right in RIGHT:
        lines[sY][sX] = ("F", 0)
    elif left and left in LEFT and right and right in RIGHT:
        lines[sY][sX] = ("-", 0)


lines = loadFile("input.txt")  # created from the clone
height, width = dimensions(lines)

clone = createClone(height, width)
sX, sY = findS(lines)
validUnchecked = [(sX, sY, 0)]


furthestDistance = markPipes(lines, clone, validUnchecked)

print(furthestDistance)


def clearOutsides(clone):
    for height, line in enumerate(clone):
        stillOutside = True
        length = len(line) - 1
        while stillOutside and length >= 0:
            if line[length][0] == ".":
                clone[height][length] = (" ", line[length][1])
            else:
                stillOutside = False

            length -= 1


# clearOutsides(clone)

changeS(clone, sX, sY)

linesPlus = []  # used for 10+
for c in clone:
    linesPlus.append("".join([x[0] for x in c]))


def isVerticallyConnected(line: str, index: int):
    curr = line[index]

    if curr in "|LJ":
        return True

    return False


isInsideCount = 0
for line in linesPlus:
    isInside = False
    thisLine = 0

    for index, char in enumerate(line):
        print(char, end="")
        if char != "." and isVerticallyConnected(line, index):
            isInside = not isInside

        elif char == "." and isInside:
            # print("#", end="")
            isInsideCount += 1
            thisLine += 1

    print(" -", thisLine)
    thisLine = 0

print(isInsideCount)

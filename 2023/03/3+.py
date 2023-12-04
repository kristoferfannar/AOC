import math


def readFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def findWidth(lines):
    return len(lines[0])


def findLength(lines):
    return len(lines)


def createGraph(lines):
    coords = []

    for line in lines:
        coord = []
        num = ""
        for char in line:
            if char.isnumeric():
                coord.append("!")
                num += char
            else:
                if num != "":
                    coord[-1] = num
                    num = ""
                coord.append(char)

        if num != "":
            coord[-1] = num
            num = ""

        coords.append(coord)
    return coords


def isSymbol(char: str):
    return not char.isnumeric() and not char == "." and not char == "!"


def isGear(char: str):
    return char == "*"


def getNumber(row: list, index, searchFurther=False):
    value = row[index]
    rowCopy = row[index+1:].copy()
    if (isSymbol(value) or value == "."):
        return []
    while value == "!":
        if not searchFurther:
            return []

        value = rowCopy.pop(0)
    return [int(value)]


def findAdjacentNumbers(x, y, graph):
    adjacentNumbers = []
    length = findLength(graph)
    width = findWidth(graph)

    aboveRow = graph[max(0, y - 1)]
    currRow = graph[y]
    belowRow = graph[min(length - 1, y + 1)]

    leftColIndex = max(0, x - 1)
    currColIndex = x
    rightColIndex = min(width - 1, x + 1)

    if (x == 136 and y == 28):
        print("here")

    adjacentNumbers += getNumber(aboveRow, leftColIndex)
    adjacentNumbers += getNumber(aboveRow, currColIndex)
    adjacentNumbers += getNumber(aboveRow, rightColIndex, searchFurther=True)

    adjacentNumbers += getNumber(currRow, leftColIndex)
    adjacentNumbers += getNumber(currRow, rightColIndex, searchFurther=True)

    adjacentNumbers += getNumber(belowRow, leftColIndex)
    adjacentNumbers += getNumber(belowRow, currColIndex)
    try:
        adjacentNumbers += getNumber(belowRow,
                                     rightColIndex, searchFurther=True)
    except IndexError:
        adjacentNumbers += getNumber(belowRow,
                                     rightColIndex, searchFurther=True)
        print("oops")

    return adjacentNumbers


lines = readFile("input.txt")

graph = createGraph(lines)

for row in graph:
    print(row)

adjSum = 0
for y, row in enumerate(graph):
    for x, value in enumerate(row):
        if isGear(value):
            numbers = findAdjacentNumbers(x, y, graph)
            if len(numbers) == 2:
                adjSum += math.prod(numbers)

print(adjSum)

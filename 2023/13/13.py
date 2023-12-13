def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def splitPatterns(lines: list[str]):
    pattern = []

    while len(lines) > 0:
        newLine = lines.pop(0)

        if newLine == "":
            return pattern

        pattern.append(newLine)

    return pattern


def transform(vert: list[str]):
    newVert = []

    for index in range(len(vert[0])):
        vertSlice = ""
        for line in vert:
            vertSlice += line[index]
        newVert.append(vertSlice)

    return newVert


def lineValue(line: str):
    value = 0
    for index, char in enumerate(line):
        if char == "#":
            value += 2 ** index

    return value


def findValues(lines: list[str]):
    values = []

    for line in lines:
        lineVal = lineValue(line)
        values.append(lineVal)

    return values


def findCenter(values: list[int]):
    for centerIndex in range(len(values)):
        distance = 0
        isCenter = True

        while isCenter and (lower := centerIndex - distance) >= 0 and (higher := centerIndex + 1 + distance) < len(values):
            if values[lower] != values[higher]:
                isCenter = False
            distance += 1

        if isCenter and not centerIndex == len(values) - 1:
            return centerIndex + 1
    return 0


lines = loadFile("input.txt")

vertSum = 0
horiSum = 0

while lines != []:
    pattern = splitPatterns(lines)
    # try vert
    vert = transform(pattern)

    vertValues = findValues(vert)
    vertCenter = findCenter(vertValues)
    vertSum += vertCenter

    if vertCenter == 0:
        horiValues = findValues(pattern)
        horiCenter = findCenter(horiValues)
        horiSum += horiCenter

answer = vertSum + horiSum * 100

print(answer)

# for line in vert:
#     print(line)

# print()

# for line in hori:
#     print(line)

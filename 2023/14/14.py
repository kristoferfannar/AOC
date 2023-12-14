import hashlib


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def transform(lines: list[str]):
    transformed = []

    for index in range(len(lines[0])):
        newLine = ""
        for line in lines:
            newLine += line[index]
        transformed.append(newLine)

    return transformed


def moveRocks(line: str, left=True):
    lastRock = 0

    newLine = ""
    while (currRock := line.find("#", lastRock)) != -1:

        substring = line[lastRock:currRock]
        movingRockCount = substring.count("O")

        os = "O" * movingRockCount
        dots = "." * (currRock - lastRock - movingRockCount)
        if left:
            newLine += os + dots + "#"
        else:
            newLine += dots + os + "#"
        lastRock = currRock + 1

    restOfLine = line[lastRock:]
    movingRocks = restOfLine.count("O")

    os = "O" * movingRocks
    dots = "." * (len(restOfLine) - movingRocks)

    if left:
        newLine += os + dots
    else:
        newLine += dots + os

    return newLine


def calculateLine(line: str):
    count = 0

    for index, char in enumerate(line):
        if char == "O":
            count += (len(line) - index)

    return count


def cycle(lines: list[str]):
    # NORTH
    transformedLines = transform(lines)  # N - S

    movedNorth = []
    for line in transformedLines:
        movedRockLine = moveRocks(line, left=True)
        movedNorth.append(movedRockLine)

    # WEST
    lines = transform(movedNorth)
    movedWest = []
    for line in lines:
        movedWestLine = moveRocks(line, left=True)
        movedWest.append(movedWestLine)

    # SOUTH
    lines = transform(movedWest)
    movedSouth = []
    for line in lines:
        movedSouthLine = moveRocks(line, left=False)  # N - S
        movedSouth.append(movedSouthLine)

    # EAST
    lines = transform(movedSouth)
    movedEast = []
    for line in lines:
        movedEastLine = moveRocks(line, left=False)
        movedEast.append(movedEastLine)

    return movedEast


def calculateCount(lines):
    lines = transform(lines)
    count = 0

    for line in lines:
        lineCount = calculateLine(line)
        count += lineCount

    return count


def cycleN(lines, n: int):
    cycledLines = lines
    values = {}

    index = 0

    while index < n:

        cycledLines = cycle(cycledLines)
        try:
            lastIndex = values.get(hashlib.sha256(
                "".join(cycledLines).encode("utf-8")).hexdigest())
            jump = index - lastIndex
            index += jump * ((n - index - 1) // jump)
        except:
            pass

        values[hashlib.sha256("".join(cycledLines).encode(
            'utf-8')).hexdigest()] = index

        index += 1

    return cycledLines


lines = loadFile("input.txt")

cycledLines = cycleN(lines, 1_000_000_000)
count = calculateCount(cycledLines)

print(count)


# print(count)

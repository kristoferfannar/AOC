def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def findRowsToAdd(lines):
    doubleRows = []
    for row, line in enumerate(lines):
        if not "#" in line:
            doubleRows.append(row)

    return doubleRows


def findColumnsToAdd(lines):
    doubleColumns = []
    for column in range(len(lines[0])):
        empty = True
        for line in lines:
            if line[column] == "#":
                empty = False

        if empty:
            doubleColumns.append(column)

    return doubleColumns


def expandSpace(lines):
    doubleRows = findRowsToAdd(lines)
    doubleColumns = findColumnsToAdd(lines)

    newSpace = []

    for row, line in enumerate(lines):
        newLine = ""
        for column, char in enumerate(line):
            newLine += char
            if column in doubleColumns:
                newLine += char

        newSpace.append(newLine)
        if row in doubleRows:
            newSpace.append(newLine)

    return newSpace


def findGalaxies(space):
    galaxies = []

    for y, line in enumerate(expandedSpace):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))
    return galaxies


def calculateDistance(gal1, gal2):
    return abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])


def findDistances(galaxies):
    distance = 0
    pairs = 0
    for thisIndex in range(len(galaxies)):
        for otherIndex in range(thisIndex + 1, len(galaxies)):
            distance += calculateDistance(galaxies[thisIndex],
                                          galaxies[otherIndex])
            pairs += 1

    print(f"{pairs} pairs found")
    return distance


lines = loadFile("input.txt")

expandedSpace = expandSpace(lines)


# for expLine in expandedSpace:
#     print(expLine)

galaxies = findGalaxies(expandedSpace)

distances = findDistances(galaxies)

print(distances)

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


def findGalaxies(space):
    galaxies = []

    for y, line in enumerate(space):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))
    return galaxies


def calculateDistance(gal1, gal2, doubleRows, doubleColumns):
    horizontalDistance = abs(gal1[0] - gal2[0])
    verticalDistance = abs(gal1[1] - gal2[1])

    for dRow in doubleRows:
        if min(gal1[1], gal1[1]) < dRow < max(gal1[1], gal2[1]):
            verticalDistance += EMPTY_DISTANCE - 1

    for dCol in doubleColumns:
        if min(gal1[0], gal2[0]) < dCol < max(gal1[0], gal2[0]):
            horizontalDistance += EMPTY_DISTANCE - 1

    return horizontalDistance + verticalDistance


def findDistances(galaxies, doubleRows, doubleColumns):
    distance = 0
    pairs = 0
    for thisIndex in range(len(galaxies)):
        for otherIndex in range(thisIndex + 1, len(galaxies)):
            newDistance = calculateDistance(galaxies[thisIndex],
                                            galaxies[otherIndex], doubleRows, doubleColumns)
            # print(f"{galaxies[thisIndex]}, {
            #       galaxies[otherIndex]} = {newDistance}")
            distance += newDistance
            pairs += 1

    print(f"{pairs} pairs found")
    return distance


EMPTY_DISTANCE = 1000000

lines = loadFile("input.txt")

doubleRows = findRowsToAdd(lines)
doubleColumns = findColumnsToAdd(lines)


galaxies = findGalaxies(lines)

# print(galaxies)

distances = findDistances(galaxies, doubleRows, doubleColumns)

print(distances)

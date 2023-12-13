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


def is_power_of_two(n):
    # This doesnt work. I cant check whether the difference is a power of two, since two bits can be different, but the difference can still be a power of two.
    # for example, 2: binary = 10, and 1: binary = 01, differ by 1 (2 - 1) which is a power of two, while still, two bits are different
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


def differs_by_one_bit(num1, num2):
    # gotten from chat, still my idea.
    xor_result = num1 ^ num2
    return (xor_result & (xor_result - 1)) == 0 and xor_result != 0


def findCenter(values: list[int], p2: bool):
    for centerIndex in range(len(values)):
        smudges = 0
        distance = 0
        isCenter = True

        while isCenter and (lower := centerIndex - distance) >= 0 and (higher := centerIndex + 1 + distance) < len(values):
            if values[lower] != values[higher]:
                isCenter = False

            if p2:
                # difference = abs(values[lower] - values[higher])

                # if is_power_of_two(difference):  # smudge found
                if differs_by_one_bit(values[lower], values[higher]):
                    smudges += 1
                    isCenter = True

            distance += 1

        if isCenter and not centerIndex == len(values) - 1:
            if p2 and smudges == 1 or not p2:
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
    vertCenter = findCenter(vertValues, p2=True)
    vertSum += vertCenter

    if vertCenter == 0:
        horiValues = findValues(pattern)
        horiCenter = findCenter(horiValues, p2=True)
        # print("H", horiCenter)
        horiSum += horiCenter
    # else:
    #     print("V", vertCenter)

answer = vertSum + horiSum * 100

print(answer)

# for line in vert:
#     print(line)

# print()

# for line in hori:
#     print(line)

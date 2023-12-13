def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def processField(field: str):
    field = field.strip(".")
    newField = ""

    for char in field:
        if not (char == "." and newField[-1] == "."):
            newField += char
    return newField


def splitter(lines: list[str]):
    splits = []

    for line in lines:
        field, counts = line.split(' ')
        field = processField(field)
        splits.append([field, counts])
    return splits


# def calcWays(field: str, counts: str):
#     # separators = counts.count(",")
#     if field == "" or counts == "":
#         return 0

#     currSize = int(counts.split(",")[0])

#     positions = list(field)

#     total = 0
#     for index, char in enumerate(positions):
#         if char == "?":
#             nextQuiz = positions[1:].index("?")

#     return total

def isValidCombination(field: str, counts: str):
    splits = field.split(".")
    lengths = [len(x) for x in splits if x != ""]
    countsInt = [int(x) for x in counts.split(',')]

    if len(lengths) == len(countsInt):
        for index in range(len(countsInt)):
            if lengths[index] != countsInt[index]:
                return False

        return True

    return False


def calcWays(field: str, counts: str):
    quizCount = field.count("?")
    combinationsLeft = 2 ** quizCount

    positions = list(field)

    validCombinations = 0

    while combinationsLeft > 0:
        countLeft = combinationsLeft
        posCopy = positions.copy()
        quizSeen = 0
        for index, char in enumerate(positions):
            if char == "?":
                quizSeen += 1
                if countLeft > 2 ** (quizCount - quizSeen):
                    posCopy[index] = "#"
                    countLeft -= 2 ** (quizCount - quizSeen)
                else:
                    posCopy[index] = "."
        combinationsLeft -= 1
        # print(posCopy, end="")
        if isValidCombination("".join(posCopy), counts):
            # print(" - valid")
            validCombinations += 1
        # else:
            # print(" - invalid")

    return validCombinations


lines = loadFile("input.txt")
splits = splitter(lines)

total = 0
for index, line in enumerate(splits):
    print(f"line {index + 1}")
    ways = calcWays(*line)
    # print(line, end=" ")
    # print(ways)
    total += ways

print(total)

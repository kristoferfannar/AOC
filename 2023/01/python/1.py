

def loadFile(filename):
    lines = []

    with open(filename, "r") as file:
        while (line := file.readline()) != "":
            lines.append(line)

    return lines


def findLineSum(line: str):
    firstNum = 0
    lastNum = 0
    firstFound = False
    for char in line:
        if char.isdigit():
            if not firstFound:
                firstNum = int(char)
                firstFound = True
            lastNum = int(char)

    return firstNum * 10 + lastNum


def findSum(lines):
    sum = 0
    for line in lines:
        sum += findLineSum(line)
    return sum


lines = loadFile("input.txt")
print(findSum(lines))

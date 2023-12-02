

def loadFile(filename):
    lines = []

    with open(filename, "r") as file:
        while (line := file.readline()) != "":
            lines.append(line)

    return lines


def findLineSum(line: str, digits: dict):
    firstNum = 0
    lastNum = 0
    firstFound = False
    for index, char in enumerate(line):
        if char.isdigit():
            if not firstFound:
                firstNum = int(char)
                firstFound = True
            lastNum = int(char)
        else:
            for key, val in digits.items():
                if line[index:].startswith(key):
                    if not firstFound:
                        firstNum = val
                        firstFound = True
                    lastNum = val

    return firstNum * 10 + lastNum


def findSum(lines, digits):
    sum = 0
    for line in lines:
        sum += findLineSum(line, digits)
    return sum


digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
          "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

lines = loadFile("input.txt")
print(findSum(lines, digits))

from operator import add, sub


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def toNumbers(line: str):
    return [int(num) for num in line.split(" ")]


def calculateSteps(numbers: list[int]):
    steps = []
    for index in range(len(numbers) - 1):
        steps.append(numbers[index+1] - numbers[index])
    return steps


def findNextNumber(numbers: list[int]):
    if not all(x == 0 for x in numbers):  # originally `if sum(numbers) != 0:` which was WRONG
        steps = calculateSteps(numbers)
        nextNumber = findNextNumber(steps)
        return numbers[-1] + nextNumber

    return 0


lines: list[str] = loadFile("input.txt")

nextSum = 0
for line in lines:
    numbers: list[int] = toNumbers(line)
    numbers.reverse()
    nextNum = findNextNumber(numbers)
    nextSum += nextNum

print(nextSum)

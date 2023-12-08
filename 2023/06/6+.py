import math

startSpeed = 0
boost = 1


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def toNumber(line: str):
    line = line.split(": ")[-1]
    nums = [num for num in line.split(" ") if num.isnumeric()]
    return int("".join(nums))


def getRaces(lines):
    times = toNumber(lines[0])
    dests = toNumber(lines[1])

    return [times, dests]


def calculateTime(time, maxTime):
    return time * (maxTime - time)


def calculateWins(maxTime, record):
    for i in range(maxTime):
        time = calculateTime(i, maxTime)
        if time > record:
            return maxTime + 1 - i * 2
    return 0


lines = loadFile("input.txt")
race = getRaces(lines)

wins = calculateWins(race[0], race[1])

print(wins)

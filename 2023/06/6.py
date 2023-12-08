import math

startSpeed = 0
boost = 1


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def toNumbers(line: str):
    line = line.split(": ")[-1]
    return [int(num) for num in line.split(" ") if num.isnumeric()]


def getRaces(lines):
    times = toNumbers(lines[0])
    dests = toNumbers(lines[1])

    return list(zip(times, dests))


lines = loadFile("input.txt")
races = getRaces(lines)


def calculateTime(time, maxTime):
    return time * (maxTime - time)


def calculateWins(maxTime, record):
    wins = 0
    for i in range(maxTime):
        time = calculateTime(i, maxTime)
        if time > record:
            wins += 1
        # print(f"start {i}: {calculateTime(i, maxTime)}")
    return wins


winList = []
for race in races:
    wins = calculateWins(race[0], race[1])
    winList.append(wins)


power = math.prod(winList)

print(winList)
print(power)

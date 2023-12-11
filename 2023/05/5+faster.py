import math
from time import time


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def getSeeds(line: str):
    return [int(number) for number in line[7:].split(" ")]


def getSourceDestRange(line: str) -> list[int, int, int]:
    numbers = [int(num) for num in line.split(" ")]
    assert len(numbers) == 3

    return numbers


def sortAndWrap(mapping: list[list[list[int]]]):
    for mapp in mapping:
        mapp.sort(key=lambda x: x[0])
        firstSrc = mapp[0][0]
        mapp.insert(0, [-math.inf, 0, firstSrc])

        lastSrc = mapp[-1][-1]
        mapp.append([lastSrc, 0, math.inf])


def mapper(lines: list[str]):
    mapper: list[list[list[int, int, int]]] = []

    currentMap = ""
    for line in lines:
        if (index := line.find(" map:")) != -1:
            mapper.append([])

        elif line != "":
            dest, src, range = getSourceDestRange(line)
            mapper[-1].append([src, dest - src, range + src])

    sortAndWrap(mapper)

    return mapper


def getDest(mapp, src):
    for mappList in mapp:
        if mappList[0] <= src < mappList[2]:
            return mappList[1] + src

    return src  # no mapping found, then return the same value


def getLocation(mapping, seed):
    src = seed
    for mapp in mapping:
        src = getDest(mapp, src)
    return src


def getSeedFromLocation(location: int):
    pass


def inRanges(seed: int):
    pass


lines = loadFile("test.txt")

seeds = getSeeds(lines.pop(0))
mapping = mapper(lines[1:])

for mapp in mapping:
    print(mapp)


location = 0

seedFound = None
while not seedFound:
    seed = getSeedFromLocation(location)
    if inRanges(seed):
        seedFound = seed
    location += 1


print(f"Lowest location: {location}")

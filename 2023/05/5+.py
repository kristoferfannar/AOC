import math


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
        if (firstSrc := mapp[0][0]) != 0:
            # mapper[currentMap].insert(0, [0, 0, firstSrc])
            mapp.insert(0, [0, 0, firstSrc])

        # lastSrc = mapper[currentMap][-1][-1]
        lastSrc = mapp[-1][-1]
        # mapper[currentMap].append([lastSrc, 0, math.inf])
        mapp.append([lastSrc, 0, math.inf])


def mapper(lines: list[str]):
    # mapper = {str: list[list[int, int, int]]}
    # mapper["seeds"] = getSeeds(lines.pop(0))
    mapper: list[list[list[int, int, int]]] = []

    currentMap = ""
    for line in lines:
        if (index := line.find(" map:")) != -1:
            # currentMap = line[:index]
            # mapper[currentMap] = []
            mapper.append([])

        elif line != "":
            dest, src, range = getSourceDestRange(line)
            # mapper[currentMap].append([src, dest - src, range + src])
            mapper[-1].append([src, dest - src, range + src])

    sortAndWrap(mapper)

    return mapper


def getDest(mapp, src):
    for mappList in mapp:
        if mappList[0] <= src < mappList[2]:
            return mappList[1] + src

    # raise Exception(f"map not found for src: {src} and map: {mapp}")
    return src  # no mapping found, then return the same value


def getLocation(mapping, seed):
    src = seed
    for mapp in mapping:
        src = getDest(mapp, src)
    return src


lines = loadFile("input.txt")

seeds = getSeeds(lines.pop(0))
mapping = mapper(lines[1:])

maps = []
newSeeds = []

for index in range(0, len(seeds), 2):
    newSeeds += range(seeds[index], seeds[index] + seeds[index+1])

print(newSeeds)


for seed in newSeeds:
    location = getLocation(mapping, seed)
    # print(f"seed: {seed} - location: {location}")
    maps.append([seed, location])

maps.sort(key=lambda x: x[1])

print(f"Lowest location: {maps[0][1]}")

from math import lcm


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def maps(lines: list[str]):
    mapper = {}
    starts = []

    for line in lines:
        source, steps = line.split(" = ")
        left, right = steps.strip("()").split(", ")
        mapper[source] = {"L": left, "R": right}
        if source.endswith("A"):
            starts.append(source)

    return mapper, starts


lines = loadFile("input.txt")

SYMBOL = lines.pop(0)

mapper, starts = maps(lines[1:])


allTries = []
print(starts)
for start in starts:
    found = False
    tries = 0
    while not found:
        for char in SYMBOL:
            tries += 1
            start = mapper[start][char]
            if start.endswith("Z"):
                found = True
                allTries.append(tries)

# lcm idea from reddit, makes sense
print(lcm(*allTries))

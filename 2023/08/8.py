def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def maps(lines: list[str]):
    mapper = {}

    for line in lines:
        source, steps = line.split(" = ")
        left, right = steps.strip("()").split(", ")
        mapper[source] = {"L": left, "R": right}

    return mapper


lines = loadFile("input.txt")

SYMBOL = lines.pop(0)

mapper = maps(lines[1:])

found = False
tries = 0
current = "AAA"
while not found:
    for char in SYMBOL:
        tries += 1
        current = mapper[current][char]
        if current == "ZZZ":
            found = True
            break


print(tries)

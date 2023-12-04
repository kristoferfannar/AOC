def getLines(filename):
    with open(filename) as file:
        return file.readlines()


def lineToGame(line: str):
    gameString = line[line.find(": ") + 2:].strip()
    return gameString.split("; ")


def roundValues(round: str):
    RGB = [0, 0, 0]
    colors = round.split(", ")

    for color in colors:
        val, colorName = color.split(" ")
        if colorName == "red":
            RGB[0] = int(val)
        if colorName == "green":
            RGB[1] = int(val)
        if colorName == "blue":
            RGB[2] = int(val)

    return RGB


def gameValues(game: list[str]):
    maxRGB = [0, 0, 0]
    for round in game:
        RGB = roundValues(round)
        maxRGB = [max(maxRGB[i], RGB[i]) for i in range(3)]

    # calculates the power of the game
    return maxRGB


def gamePower(rgb):
    sum = 1
    for val in rgb:
        sum *= val

    return sum


# lines = getLines("test.txt")
lines = getLines("input.txt")

sum = 0

for line in lines:
    game = lineToGame(line)
    maxVal: list = gameValues(game)

    print(f"{str(maxVal):>14}", "; ".join(game))
    sum += gamePower(maxVal)

print(sum)

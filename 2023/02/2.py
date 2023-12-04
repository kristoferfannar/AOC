def getLines(filename):
    with open(filename) as file:
        return file.readlines()


def lineToGame(line: str):
    gameString = line[line.find(": ") + 2:-1]
    return gameString.split("; ")


def roundIsValid(round: str):
    colors = round.split(", ")
    for color in colors:
        val, colorName = color.split(" ")
        if colorName == "blue" and int(val) > BLUE:
            # print("False, ", end="")
            return False
        if colorName == "red" and int(val) > RED:
            # print("False, ", end="")
            return False
        if colorName == "green" and int(val) > GREEN:
            # print("False, ", end="")
            return False
    # print("True, ", end="")
    return True


def gameIsValid(game: list[str]):
    for round in game:
        if not roundIsValid(round):
            return False
    return True


RED = 12
GREEN = 13
BLUE = 14

lines = getLines("input.txt")

sum = 0

for index, line in enumerate(lines):
    game = lineToGame(line)
    if gameIsValid(game):
        # print(" - valid")
        sum += index + 1
    # else:
        # print(" - invalid")

print(sum)

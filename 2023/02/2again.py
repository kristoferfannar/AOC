def readFile(filename):
    with open(filename) as file:
        return file.readlines()


def getGame(line: str):
    strippedLine = line.strip()
    _, game = strippedLine.split(": ")
    return game


def splitGameIntoRounds(game):
    return game.split("; ")


def splitRoundIntoColors(round):
    return round.split(", ")


def isColorValid(color):
    """
     input| color: "3 blue"
    output| boolean: True/False    
    """
    value, name = color.split(" ")
    if name == "blue" and int(value) > BLUE:
        return False
    if name == "green" and int(value) > GREEN:
        return False
    if name == "red" and int(value) > RED:
        return False

    return True


def gameIsValid(game):
    """
    input| game = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    output| boolean = True/False
    """
    rounds = splitGameIntoRounds(game)
    # rounds = ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]

    colorCount: list = []
    for round in rounds:
        # round = 3 blue, 4 red
        colorCount += splitRoundIntoColors(round)
        # colorCount = ["3 blue", "4 red"]

    for color in colorCount:
        # color = "3 blue"
        if not isColorValid(color):
            return False
    return True


RED = 12
GREEN = 13
BLUE = 14

lines = readFile("input.txt")

sum = 0
for index, line in enumerate(lines):
    # line = Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    game = getGame(line)
    # game = 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    gameNumber = index + 1

    if gameIsValid(game):
        sum += gameNumber


print("sum:", sum)

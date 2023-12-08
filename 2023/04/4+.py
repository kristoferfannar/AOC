import re


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def toGames(lines: list):
    games = []
    for line in lines:
        game = line.split(": ")[1]
        game = game.split(" | ")
        winners = re.findall(r"\d+", game[0])
        guesses = re.findall(r"\d+", game[1])
        games.append([[int(guess) for guess in guesses], [
                     int(winner) for winner in winners]])

    return games


def findMatches(guesses, game):
    matches = 0
    for guess in guesses:
        if guess in game:
            # print(guess, end=" ")
            matches += 1
    return matches


lines = loadFile("input.txt")
games = toGames(lines)

copies = [1] * len(lines)

for index, game in enumerate(games):
    matches = findMatches(game[0], game[1])

    for i in range(index + 1, index + matches + 1):
        copies[i] += copies[index]


print(sum(copies))

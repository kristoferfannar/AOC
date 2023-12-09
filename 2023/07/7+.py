ORDER = "J23456789TJQKA"


def loadFile(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def getHands(lines: list[str]):
    return [line.split(" ") for line in lines]


def getType(hand: str) -> int:
    cards = list(hand)
    cardCount = {}

    for card in cards:
        try:
            cardCount[card] += 1
        except:
            cardCount[card] = 1

    # find the amount of jokers
    jokers = 0
    if cardCount.get("J") != None:
        jokers = cardCount["J"]
        # remove the jokers from the count
        del cardCount["J"]

    counts = list(cardCount.values())
    print(counts, hand)
    counts.sort(reverse=True)

    # add jokers to most significant value
    if len(counts) != 0:
        counts[0] += jokers
    else:
        counts = [jokers]

    if counts[0] == 5:  # five of a kind
        return 6

    if counts[0] == 4:  # four of a kind
        return 5

    if counts[0] == 3 and counts[1] == 2:  # full house
        return 4

    if (len(counts) == 3):
        if counts[0] == 3:  # three of a kind
            return 3

        if counts[0] == 2 and counts[1] == 2:  # two pair
            return 2

    if len(counts) == 4 and counts[0] == 2:  # one pair
        return 1

    if len(counts) == 5 and counts[0] == 1:  # singles
        return 0

    raise Exception("error: ", hand)


def orderHand(hand):
    type = getType(hand[0])

    firstCard = ORDER.find(hand[0][0])
    secondCard = ORDER.find(hand[0][1])
    thirdCard = ORDER.find(hand[0][2])
    fourthCard = ORDER.find(hand[0][3])
    fifthCard = ORDER.find(hand[0][4])

    return type, firstCard, secondCard, thirdCard, fourthCard, fifthCard


def calculateRank(hands: list):
    rank = 0

    for index, hand in enumerate(hands):
        rank += (index + 1) * int(hand[1])

    return rank


lines = loadFile("input.txt")
hands = getHands(lines)
hands.sort(key=orderHand)

rank = calculateRank(hands)

print(rank)

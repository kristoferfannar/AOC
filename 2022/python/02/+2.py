WIN = 6
DRAW = 3
LOSS = 0
ROCK = 1
PAPER = 2
SCISSORS = 3
#FILENAME = "2_input.txt"
FILENAME = "input.txt"

def main():
    lines = read_from_file()
    score = 0
    for line in lines:
        score += calculate_score(line[0], line[1])
        
    print(score)


def read_from_file():
    lines = []

    with open (FILENAME, 'r') as file:
        lines = file.readlines()
    
    return [i.strip().split(' ') for i in lines]



def calculate_score(p1, p2):
    if p2 == "X":
        if p1 == "A":
            return SCISSORS + LOSS
        if p1 == "B":
            return ROCK + LOSS
        if p1 == "C":
            return PAPER + LOSS

    if p2 == "Y":
        if p1 == "A":
            return ROCK + DRAW
        if p1 == "B":
            return PAPER + DRAW
        if p1 == "C":
            return SCISSORS + DRAW

    if p2 == "Z":
        if p1 == "A":
            return PAPER + WIN
        if p1 == "B": 
            return SCISSORS + WIN
        if p1 == "C":
            return ROCK + WIN

    raise Exception()

if __name__ == "__main__":
    main()

FILENAME = 'input.txt'
#FILENAME = 'test_input.txt'


def main():
    lines = read_from_file()
    score = 0

    for line in lines:
        wrong_item: str = find_wrong_item(line)
        score += calculate_item_priority(wrong_item)

    print(score)


def find_wrong_item(line: str):
    comp1 = line[0: len(line) // 2]
    comp2 = line[len(line) // 2 :]
    
    for letter in comp2:
        if letter in comp1:
            return letter

    raise Exception()



def read_from_file():
    lines = []

    with open (FILENAME, 'r') as file:
        lines = file.readlines()

    return [i.strip() for i in lines]



def calculate_item_priority(item: str):
    item = item.swapcase()
    
    subtracter = 64
    if ord(item) - subtracter > 26:
        subtracter += 6
    return ord(item) - subtracter




if __name__ == "__main__":
    main()

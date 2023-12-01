FILENAME = 'input.txt'
#FILENAME = 'test_input.txt'


def main():
    lines = read_from_file()
    score = 0

    for index in range(0, len(lines), 3):
        line1 = lines[index]
        line2 = lines[index + 1]
        line3 = lines[index + 2]

        wrong_item: str = find_wrong_item(line1, line2, line3)
        score += calculate_item_priority(wrong_item)

    print(score)


def find_wrong_item(line1: str, line2: str, line3: str):
    
    for letter in line3:
        if letter in line1 and letter in line2:
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

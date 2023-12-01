FILENAME = 'input.txt'
FILENAME = 'test_input.txt'


def main():
    print(read_from_file())


def read_from_file():
    lines = []

    with open(FILENAME, 'r') as file:
        lines = file.readlines()

    return [line.strip().split(',') for line in lines]




if __name__ == "__main__":
    main()

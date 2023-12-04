import re


def loadFile(filename):
    with open(filename) as file:
        return file.readlines()


lines = loadFile("input.txt")

numbers = []
for line in lines:
    nums = re.findall(r'\d+', line)
    numbers += [int(num) for num in nums]


numbers.sort()
numberSet = set(numbers)

print(len(numberSet))
print(len(numbers))

import sys

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readline():
    line = ""
    with open(file) as f:
        line = f.readline()

    return line.strip()


line = readline()


blocks = []


idx = 0
id = 0
while idx < len(line):
    if idx % 2 == 0:
        blocks.extend([f"{id}"] * int(line[idx]))
        id += 1
    else:
        blocks.extend(["."] * int(line[idx]))

    idx += 1


front = 0
back = len(blocks) - 1


while front < back:
    while blocks[front] != ".":
        front += 1

    while blocks[back] == ".":
        back -= 1

    if front >= back:
        break

    blocks[front], blocks[back] = blocks[back], blocks[front]
    # print("".join(["".join(block) for block in blocks]))


total = 0
for idx in range(back + 1):
    total += idx * int(blocks[idx])

print(total)

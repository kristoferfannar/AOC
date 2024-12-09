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
ids = []

idx = 0
id = 0
while idx < len(line):
    if idx % 2 == 0:
        ids.append(dict())

        ids[id]["idx"] = len(blocks)
        ids[id]["used"] = int(line[idx])

        blocks.extend([f"{id}"] * int(line[idx]))
    else:
        blocks.extend(["."] * int(line[idx]))
        ids[id]["free"] = int(line[idx])
        id += 1

    idx += 1


front = 0
back = len(blocks) - 1


# print("".join(["".join(block) for block in blocks]))
for id in range(len(ids) - 1, -1, -1):
    for i in range(id):
        if ids[i]["free"] >= ids[id]["used"]:
            i_start = ids[i + 1]["idx"] - ids[i]["free"]
            i_end = ids[i + 1]["idx"]
            id_start = ids[id]["idx"]
            if id + 1 < len(ids):
                id_end = ids[id + 1]["idx"]
            else:
                id_end = len(blocks) - 1

            for _ in range(ids[id]["used"]):
                blocks[i_start], blocks[id_start] = blocks[id_start], blocks[i_start]
                i_start += 1
                id_start += 1

            ids[i]["free"] -= ids[id]["used"]

            break


total = 0
for idx in range(back + 1):
    if blocks[idx] != ".":
        total += idx * int(blocks[idx])

print(total)

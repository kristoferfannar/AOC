import sys

if len(sys.argv) != 2:
    exit()
file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def to_cmb(item: list[str], breaker):
    R = len(item)
    C = len(item[0])
    vals = []
    for c in range(C):
        val = 0
        for r in range(1, R):
            if item[r][c] == breaker:
                break
            val += 1
        vals.append(val)

    return tuple(vals)


def matches(lock, key):
    for i in range(len(lock)):
        if lock[i] > key[i]:
            return False
    return True


locks = set()
keys = set()
item = []
for line in readlines() + [""]:  # add empty str so that last item is processed
    if line == "":
        if item[0][0] == "#":
            locks.add(to_cmb(item, breaker="."))
        else:
            keys.add(to_cmb(item, breaker="#"))
        item = []
    else:
        item.append(line)


total = 0
for lock in locks:
    for key in keys:
        if matches(lock, key):
            total += 1
print(total)

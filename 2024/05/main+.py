def readlines():
    lines = []
    with open("in.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


lines = readlines()

rules = []
prints = []
for idx, line in enumerate(lines):
    if line == "":
        rules = [[int(x) for x in l.split("|")] for l in lines[:idx]]
        prints = [[int(x) for x in l.split(",")] for l in lines[idx + 1 :]]

before = dict()
after = dict()

for f, s in rules:
    if f not in after:
        after[f] = set()
    if s not in before:
        before[s] = set()
    after[f].add(s)
    before[s].add(f)


def find_mid(p: list):
    left = p.copy()
    new = []

    while left:
        for i in range(len(left)):
            next = True
            # nobody comes before this number
            if left[i] not in before:
                new.append(left[i])
                left.pop(i)
                break

            for j in range(i + 1, len(left)):
                if left[i] not in after or left[j] in before[left[i]]:
                    next = False
                    break

            if next:
                new.append(left[i])
                left.pop(i)
                break

    return new[len(new) // 2]


total = 0
for p in prints:
    valid = True
    curr = set()

    for num in p:
        if num in after and after[num].intersection(curr):
            valid = False
            break
        curr.add(num)

    if not valid:
        total += find_mid(p)

print(total)

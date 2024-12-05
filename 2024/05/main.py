def readlines():
    lines = []
    with open("in.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


lines = readlines()

rules = []
prints = []
for idx, line in enumerate(lines):
    print(line)
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


total = 0
for p in prints:
    valid = True
    curr = set()

    for num in p:
        if num in after and after[num].intersection(curr):
            valid = False
            break
        curr.add(num)

    if valid:
        total += p[len(p) // 2]

print(total)

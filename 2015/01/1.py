import sys

if len(sys.argv) != 2:
    exit(1)

file = sys.argv[-1]


def readline():
    with open(file) as f:
        return f.readline()


line = readline()

total = 0
p2 = -1
for i, brac in enumerate(line):
    if brac == "(":
        total += 1
    elif brac == ")":
        total -= 1

    if total == -1 and p2 == -1:
        p2 = i + 1

print(total)
print(p2)

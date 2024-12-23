import sys
from collections import defaultdict

if len(sys.argv) != 2:
    exit(0)

file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    return [int(line.strip()) for line in lines]


def mix(num, secret):
    return num ^ secret


def prune(num):
    return num % 16777216


lines = readlines()
totals = defaultdict(lambda: 0)  # dict with every combination of sequences
p1 = 0
for num in lines:
    seqs = dict()
    last = num % 10
    nexts = []

    for _ in range(2000):
        # step 1
        num = mix(num * 64, num)
        num = prune(num)
        # step 2
        num = mix(num // 32, num)
        num = prune(num)
        # step 3
        num = mix(num * 2048, num)
        num = prune(num)

        val = num % 10

        nexts.append(val - last)
        if len(nexts) == 5:
            nexts.pop(0)
            if tuple(nexts) not in seqs:
                seqs[tuple(nexts)] = val

        last = val

    p1 += num

    for seq, val in seqs.items():
        totals[seq] += val

print("p1", p1)
print("p2", max(totals.values()))

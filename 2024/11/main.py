import sys
from functools import cache
from math import ceil, log10

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    line = ""
    with open(file) as f:
        line = f.readline()

    return [int(x) for x in line.strip().split()]


line = readlines()


# @cache
# def convert(nums, times):
#     return


def split(num):
    return [
        int(str(num)[: len(str(num)) // 2]),
        int(str(num)[len(str(num)) // 2 :]),
    ]


total = 0
for i in range(len(line)):
    lis = [line[i]]
    for _ in range(20):
        new = []
        for num in lis:
            if num == 0:
                new.append(1)
            elif len(str(num)) % 2 == 0:
                new.extend(split(num))

            else:
                new.append(num * 2024)

        lis = new

    # print(f"{line[i]} -> {lis}")
    total += len(lis)

print(total)

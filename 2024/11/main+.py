import sys
from functools import cache, lru_cache
from math import ceil, log10
from itertools import chain

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


# @lru_cache(2**20)
# def convert(num, times):
#     if times == 0:
#         return [num]
#
#     if num == 0:
#         return convert(1, times - 1)
#
#     if num > 1 and ceil(log10(num)) % 2 == 0:
#         return list(chain.from_iterable(convert(n, times - 1) for n in split(num)))
#
#     return convert(num * 2024, times - 1)


@lru_cache(2**20)
def convert(num, times):
    if times == 0:
        return 1

    if num == 0:
        return convert(1, times - 1)

    # if num > 1 and ceil(log10(num)) % 2 == 0:
    if len(str(num)) % 2 == 0:
        converted = [convert(n, times - 1) for n in split(num)]
        return sum(converted)

    return convert(num * 2024, times - 1)


def split(num):
    return [int(str(num)[: len(str(num)) // 2]), int(str(num)[len(str(num)) // 2 :])]
    # digits = ceil(log10(num))
    # return (num // 10 ** (digits // 2), num % 10 ** (digits // 2))


total = 0
for i in range(len(line)):
    lis = [line[i]]
    for num in lis:
        added = convert(num, 75)
        # print(f"{num} -> {lis}")
        total += added

print(total)

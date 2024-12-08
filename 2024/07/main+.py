import sys
from tqdm import tqdm

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    return lines


lines = readlines()


def shift(num):
    shifter = 0

    while num > 0:
        shifter += 1
        num //= 10

    return 10**shifter


def is_valid(test, nums, idx=0, curr=0):
    if len(nums) == idx:
        return curr == test

    plus = curr + nums[idx]
    mult = max(curr, 1) * nums[idx]
    join = curr * shift(nums[idx]) + nums[idx]

    return (
        is_valid(test, nums, idx + 1, plus)
        or is_valid(test, nums, idx + 1, mult)
        or is_valid(test, nums, idx + 1, join)
    )


total = 0
for line in tqdm(lines):
    test, nums = line.strip("\n").split(": ")
    test = int(test)
    nums = [int(num) for num in nums.split(" ")]

    if is_valid(test, nums):
        total += test

print(total)

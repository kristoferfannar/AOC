import sys

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


def is_valid(test, nums, idx=0, curr=0):
    if len(nums) == idx:
        return curr == test

    return is_valid(test, nums, idx + 1, curr + nums[idx]) or is_valid(
        test, nums, idx + 1, max(curr, 1) * nums[idx]
    )


total = 0
for line in lines:
    test, nums = line.strip("\n").split(": ")
    test = int(test)
    nums = [int(num) for num in nums.split(" ")]

    if is_valid(test, nums):
        total += test

print(total)

import heapq


def readlines():
    lines = []
    with open("test_input.txt", "r") as file:
        lines = [[int(x) for x in n.strip().split()] for n in file.readlines()]
    return lines


lines = readlines()


ls = []
rs = []

for l, r in lines:
    heapq.heappush(ls, l)
    heapq.heappush(rs, r)


diff = 0
while ls:
    diff += abs(heapq.heappop(ls) - heapq.heappop(rs))

print(diff)

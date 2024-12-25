import sys
from heapq import heappush, heappop

if len(sys.argv) != 2:
    exit()
file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get(vars, var) -> int:
    val = vars[var]
    if isinstance(val, int):
        return val

    val1, op, val2 = val

    match op:
        case "AND":
            val = get(vars, val1) & get(vars, val2)
        case "OR":
            val = get(vars, val1) | get(vars, val2)
        case "XOR":
            val = get(vars, val1) ^ get(vars, val2)

    vars[var] = val  # update vars value so that we don't have to redo the search
    return val


vars = dict()
zs = []

lined = False
for line in readlines():
    if line == "":
        lined = True

    elif not lined:
        var, val = line.split(": ")
        vars[var] = int(val)

        if var[0] == "z":
            heappush(zs, var)
    else:
        expr, var = line.split(" -> ")
        var1, op, var2 = expr.split(" ")
        vars[var] = (var1, op, var2)

        if var[0] == "z":
            heappush(zs, var)

shift = 0
total = 0
while zs:
    z = heappop(zs)
    total += get(vars, z) << shift
    shift += 1

print(total)

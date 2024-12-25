import sys
from heapq import heappush, heappop
from collections import defaultdict
from time import sleep

if len(sys.argv) != 2:
    exit()
file = sys.argv[-1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get(vars, var, seen=None) -> int:
    if not seen:  # to detect cycles
        seen = set()

    if var in seen:  # cycle detected
        raise Exception("cycle detected")

    seen.add(var)

    val = vars[var]
    if isinstance(val, int):
        return val

    val1, op, val2 = val

    if op == "AND":
        val = get(vars, val1, seen.copy()) & get(vars, val2, seen.copy())
    elif op == "OR":
        val = get(vars, val1, seen.copy()) | get(vars, val2, seen.copy())
    elif op == "XOR":
        val = get(vars, val1, seen.copy()) ^ get(vars, val2, seen.copy())

    vars[var] = val  # update vars value so that we don't have to redo the search
    return val


vars = dict()
xs = []
ys = []
zs = []
unknown = []

lined = False
for line in readlines():
    if line == "":
        lined = True

    elif not lined:
        var, val = line.split(": ")
        vars[var] = int(val)

        if var[0] == "z":
            heappush(zs, var)
        if var[0] == "x":
            xs.append(var)
        if var[0] == "y":
            ys.append(var)
    else:
        expr, var = line.split(" -> ")
        var1, op, var2 = expr.split(" ")
        vars[var] = (var1, op, var2)

        unknown.append(var)

        if var[0] == "z":
            heappush(zs, var)
        if var[0] == "x":
            xs.append(var)
        if var[0] == "y":
            ys.append(var)


xs.sort()
ys.sort()
total = 0


def setxy(vars, xs, ys):
    """creates vars dict with every x & y idx bit set on its own"""
    for i in range(len(xs)):
        cvars = vars.copy()
        for j in range(len(xs)):
            cvars[xs[j]] = int(i == j)
            cvars[ys[j]] = int(i == j)

        yield cvars  # first time using yield


def getx(vars):
    X = 0
    cxs = xs.copy()
    for shift in range(len(cxs)):
        x = cxs[shift]
        X += vars[x] << shift  # no need to use get(), x is defined
    return X


def gety(vars):
    Y = 0
    cys = ys.copy()
    for shift in range(len(cys)):
        y = ys[shift]
        Y += vars[y] << shift  # no need to use get(), y is defined
    return Y


def Z(vars):
    zz = 0
    shift = 0
    czs = zs.copy()
    cvars = vars.copy()
    while czs:
        z = heappop(czs)
        zz += get(cvars, z) << shift
        shift += 1

    return zz


def cnv(inp: list[tuple[int, ...]]) -> tuple[int]:
    outp = []
    for i in inp:
        outp.extend(list(i))
    outp.sort()
    return tuple(outp)


def swap(vars, var1, var2):
    vars[var1], vars[var2] = vars[var2], vars[var1]


def distance(value):
    "counts the bit distance == number of set bits in value"
    dist = 0
    while value:
        dist += value & 1
        value = value >> 1

    return dist


def swapper(vars, unknown, pairs) -> list[tuple[float, tuple[int, int]]]:
    global cache
    bests = defaultdict(lambda: 0)
    its = 0
    ccvars = vars.copy()
    for cvars in setxy(ccvars, xs, ys):
        its += 1
        X, Y = getx(cvars), gety(cvars)

        if its % 11 == 0:  # debug output
            print(f"x,y={its}/{len(xs)}")

        for i in range(len(unknown)):
            for j in range(i + 1, len(unknown)):
                ccvars = cvars.copy()

                item = cnv(pairs + [(unknown[i], unknown[j])])
                if item in cache:
                    if its == 1:
                        print(f"{item} already in cache")
                    continue

                swap(ccvars, unknown[i], unknown[j])

                try:
                    zz = Z(ccvars)
                except Exception:
                    continue  # ignore cycles

                swapscore = distance((X & Y) ^ zz)
                bests[(i, j)] += swapscore

    return sorted(
        [(score / its, pair) for pair, score in bests.items()], key=lambda x: x[0]
    )


def add_to_cache(swapp):
    global cache
    for score, swap in swapp:
        pass


BREADTH = 2
success = 0
count = 0
cache: set[tuple[int]] = set()

swaps = swapper(vars, unknown, pairs=[])

for score, swapp in swaps[:BREADTH]:
    print(count)
    count += 1
    if success:
        break
    cvars = vars.copy()

    p1, p2 = unknown[swapp[0]], unknown[swapp[1]]
    swap(cvars, p1, p2)
    pairs = [(p1, p2)]

    cunknown = unknown.copy()
    cunknown.pop(swapp[0])
    cunknown.pop(swapp[1] - 1)

    swaps2 = swapper(cvars, cunknown, pairs)

    for score2, swapp2 in swaps2[:BREADTH]:
        if success:
            break
        cvars2 = cvars.copy()

        p1, p2 = cunknown[swapp2[0]], cunknown[swapp2[1]]
        swap(cvars2, p1, p2)
        pairs.append((p1, p2))

        cache.add(cnv(pairs))
        # print(f"adding {cnv(pairs)} to cache (size={len(cache)})")

        cunknown2 = cunknown.copy()
        cunknown2.pop(swapp2[0])
        cunknown2.pop(swapp2[1] - 1)

        if score2 == 0:
            print(f"found perfect match with swaps {pairs}")
            success = 1
            finalscore = score2
            break

        swaps3 = swapper(cvars2, cunknown2, pairs)

        for score3, swapp3 in swaps3[:BREADTH]:
            if success:
                break
            cvars3 = cvars2.copy()
            p1, p2 = cunknown2[swapp3[0]], cunknown2[swapp3[1]]
            swap(cvars3, p1, p2)
            pairs.append((p1, p2))

            cache.add(cnv(pairs))
            # print(f"adding {cnv(pairs)} to cache (size={len(cache)})")

            cunknown3 = cunknown.copy()
            cunknown3.pop(swapp3[0])
            cunknown3.pop(swapp3[1] - 1)

            swaps4 = swapper(cvars3, cunknown3, pairs)
            # add_to_cache(swaps4)
            finalscore, finalswapp = swaps4[0]

            if finalscore == 0:
                p1, p2 = cunknown3[finalswapp[0]], cunknown3[finalswapp[1]]
                print(f"found perfect match with swaps {list(pairs) + [(p1, p2)]}")
                success = 1
                break

            pairs.pop()

        pairs.pop()


final = []
for pair in pairs:
    final.extend(list(pair))
print(",".join(sorted(final)), finalscore)

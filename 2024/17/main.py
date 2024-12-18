import sys
import re
from typing import ParamSpecArgs

if len(sys.argv) != 2:
    print(f"input file missing")
    exit()

file = sys.argv[1]


def readlines():
    lines = []
    with open(file) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def combo(num, a, b, c):
    if num <= 3:
        return num
    elif num == 4:
        return a
    elif num == 5:
        return b
    elif num == 6:
        return c

    raise Exception("not possible")


lines = readlines()

a = int(re.findall("\d+", lines[0])[0])
b = int(re.findall("\d+", lines[1])[0])
c = int(re.findall("\d+", lines[2])[0])

ops = list(map(int, lines[4][len("Program: ") :].split(",")))

ip = 0

print(ops)

out = []
while ip < len(ops):
    operator = ops[ip]
    operand = ops[ip + 1]

    match operator:
        case 0:
            det = combo(operand, a, b, c)
            a = a // (2**det)
        case 1:
            b = b ^ operand
        case 2:
            mod = combo(operand, a, b, c)
            b = mod % 8
        case 3:
            if a != 0:
                if ip != operand:
                    ip = operand
                    continue
        case 4:
            b = b ^ c
        case 5:
            coop = combo(operand, a, b, c)
            out.append(coop % 8)
        case 6:
            det = combo(operand, a, b, c)
            b = a // (2**det)
        case 7:
            det = combo(operand, a, b, c)
            c = a // (2**det)
    ip += 2


print(",".join(map(str, out)))

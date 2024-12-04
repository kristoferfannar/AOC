def readline():
    lines = ""
    with open("in") as f:
        lines = f.readlines()
    return lines


lines = readline()


def check_mul(line: str, start):
    first = second = 0

    curr = start
    comma = False
    while curr < len(line):
        if not line[curr].isdigit():
            if not comma and line[curr] == ",":  # second number
                comma = True
            elif line[curr] == ")":  # end
                break
            else:  # invalid
                return 0
        else:
            if not comma:
                first = first * 10 + int(line[curr])
            else:
                second = second * 10 + int(line[curr])
        curr += 1

    return first * second


muls = 0
enabled = True
for line in lines:
    for start in range(len(line)):
        do = "do()"
        dont = "don't()"
        if line[start : start + len(do)] == do:
            enabled = True
        elif line[start : start + len(dont)] == dont:
            enabled = False

        if not enabled:
            continue

        pre = "mul("

        if line[start : start + len(pre)] == pre:
            mul = check_mul(line, start + len(pre))
            if not mul == 0:
                muls += mul


print(muls)

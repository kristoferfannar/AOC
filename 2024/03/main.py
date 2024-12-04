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
        # print(f"line[{curr}] = {line[curr]}")
        if not line[curr].isdigit():
            if not comma and line[curr] == ",":  # second number
                comma = True
            elif line[curr] == ")":  # end
                break
            else:  # invalid
                # print(f"invalid")
                return 0
        else:
            if not comma:
                first = first * 10 + int(line[curr])
            else:
                second = second * 10 + int(line[curr])
        curr += 1

    # print(f"first={first} second={second}")
    return first * second


muls = 0
for line in lines:
    for start in range(len(line)):
        pre = "mul("
        if line[start : start + len(pre)] == pre:
            # print(f"line[{start}] is mul(")
            mul = check_mul(line, start + len(pre))
            # print(f"mul is {mul}")
            if not mul == 0:
                print(f"{line[start: start + len(pre) + 2 + 6]} = {mul}")
                muls += mul
            else:
                print(f"! {line[start: start + len(pre) + 2 + 6]}")


print(muls)

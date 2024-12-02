def readlines():
    lines = []
    with open("input.txt", "r") as file:
        lines = [[int(x) for x in line.strip().split()] for line in file.readlines()]
    return lines


def solve(lines):
    ans = 0

    for line in lines:
        # print(f"line: {line}")
        valid = True
        decreasing = line[0] > line[-1]

        for idx in range(len(line) - 1):
            if decreasing:
                if not (1 <= line[idx] - line[idx + 1] <= 3):
                    # print(
                    #     f"line[{idx}]({line[idx]}) - line[{idx+1}]({line[idx+1]}) = {line[idx] - line[idx+1]}"
                    # )
                    valid = False
                    break
            else:
                if not (1 <= line[idx + 1] - line[idx] <= 3):
                    # print(
                    #     f"line[{idx+1}]({line[idx+1]}) - line[{idx}]({line[idx]}) = {line[idx+1] - line[idx]}"
                    # )
                    valid = False
                    break

        if valid:
            # print(f"valid!")
            ans += 1

    print(ans)


lines = readlines()
solve(lines)

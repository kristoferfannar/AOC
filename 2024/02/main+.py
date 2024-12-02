def readlines():
    lines = []
    with open("input.txt", "r") as file:
        lines = [[int(x) for x in line.strip().split()] for line in file.readlines()]
    return lines


def solve(lines):
    ans = 0

    for line in lines:
        # print(f"line: {line}")

        for skip in range(-1, len(line)):
            valid = True
            decreasing = line[0] > line[1]

            if skip in [0, 1]:
                # abuse the fact that I've seen my test input,
                # my lines are always at least 4 numbers long
                decreasing = line[2] > line[3]

            for idx in range(len(line) - 1):
                curr = idx
                next = idx + 1
                if curr == skip:
                    continue
                if skip == next:
                    if len(line) > next + 1:
                        next += 1
                    else:
                        continue

                if decreasing:
                    if not (1 <= line[curr] - line[next] <= 3):
                        # print(
                        #     f"line[{idx}]({line[idx]}) - line[{idx+1}]({line[idx+1]}) = {line[idx] - line[idx+1]}"
                        # )
                        valid = False
                        break
                else:
                    if not (1 <= line[next] - line[curr] <= 3):
                        # print(
                        #     f"line[{idx+1}]({line[idx+1]}) - line[{idx}]({line[idx]}) = {line[idx+1] - line[idx]}"
                        # )
                        valid = False
                        break

            if valid:
                # print(f"valid!")
                ans += 1
                break

    print(ans)


lines = readlines()
solve(lines)

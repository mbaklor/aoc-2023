input_file = "data-d1"


def FindEdgeNumber(s: str, inverted: bool) -> str:
    string = s
    if inverted:
        string = reversed(s)
    for c in string:
        if c.isnumeric():
            return c
    return ""


def GetCombination(s: str) -> str:
    first = FindEdgeNumber(s, False)
    last = FindEdgeNumber(s, True)
    return first + last


if __name__ == "__main__":
    sum = 0
    with open(input_file, "r") as input:
        for line in input.readlines():
            ln = line.strip()
            if ln == "":
                continue
            combo = GetCombination(ln)
            sum += int(combo)

    print(sum)

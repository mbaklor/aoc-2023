input_file = "data-d1"


def NumberWords(s: str) -> str:
    wordMap = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    if s[:5] in wordMap:
        return wordMap[s[:5]]
    if s[:4] in wordMap:
        return wordMap[s[:4]]
    if s[:3] in wordMap:
        return wordMap[s[:3]]
    return ""


def FindEdgeNumber(s: str, inverted: bool) -> str:
    string = s
    if inverted:
        string = reversed(s)
    for i, c in enumerate(string):
        start = i
        if inverted:
            start = len(s) - 1 - i
        if c.isnumeric():
            return c
        else:
            if start + 3 > len(s):
                continue
            num = NumberWords(s[start:])
            if num != "":
                return num
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

    # sum = GetCombination("tnine123blahsevenhblah2one")
    print(sum)

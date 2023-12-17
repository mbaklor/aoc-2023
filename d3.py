# input_file = "input"
input_file = "data-d3"


def get_full_num(line: str, col: int) -> int:
    idx = col - 1
    revNum = ""
    while idx >= 0 and line[idx].isnumeric():
        revNum += line[idx]
        idx -= 1
    num = ""
    idx = col
    for i in range(len(revNum), 0, -1):
        num += revNum[i - 1]
    while idx < len(line) and line[idx].isnumeric():
        num += line[idx]
        idx += 1
    return int(num)


def is_symbol(ch: str):
    period = ch == "."
    return not period


def check_char(lines: list[str], row: int, col: int) -> int:
    firstNum = 0
    secondNum = 0
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                continue
            if row + r < 0 or col + c < 0:
                continue
            if row + r > len(lines) - 1 or col + c > len(lines[row + r].strip()) - 1:
                continue
            line = lines[row + r].strip()
            if line[col + c].isnumeric():
                num = get_full_num(line, col + c)
                if firstNum == 0:
                    firstNum = num
                elif num != firstNum:
                    secondNum = num
    return firstNum * secondNum


if __name__ == "__main__":
    with open(input_file, "r") as schematic:
        lines = schematic.readlines()
        current_num = 0
        sum = 0
        for row, line in enumerate(lines):
            line = line.strip()
            for col, ch in enumerate(line):
                if ch == "*":
                    gear = check_char(lines, row, col)
                    sum += gear
        print(sum)

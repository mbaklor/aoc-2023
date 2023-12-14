# input_file = "input"
input_file = "data-d3"


def get_full_num(line: str, col: int) -> tuple[int, int]:
    idx = col
    num = ""
    while idx < len(line) and line[idx].isnumeric():
        num += line[idx]
        idx += 1
    return int(num), len(num)


def is_symbol(ch: str):
    period = ch == "."
    return not period


def check_char(lines: list[str], row: int, col: int) -> bool:
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                continue
            if row + r < 0 or col + c < 0:
                continue
            if row + r > len(lines) - 1 or col + c > len(lines[row + r].strip()) - 1:
                continue
            line = lines[row + r].strip()
            ch = line[col + c]
            if ch.isnumeric():
                continue
            if is_symbol(ch):
                return True
    return False


if __name__ == "__main__":
    with open(input_file, "r") as schematic:
        lines = schematic.readlines()
        current_num = 0
        sum = 0
        for row, line in enumerate(lines):
            line = line.strip()
            num_len = 0
            for col, ch in enumerate(line):
                if num_len > 0:
                    num_len -= 1
                    continue
                if ch.isnumeric():
                    current_num, num_len = get_full_num(line, col)
                    has_sumbol = False
                    for c in range(num_len):
                        if check_char(lines, row, col + c):
                            has_sumbol = True
                            break
                    if has_sumbol:
                        sum += current_num
        print(sum)

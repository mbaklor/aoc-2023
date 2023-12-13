from dataclasses import dataclass

# input_file = "input"
input_file = "data-d2"


@dataclass
class dice:
    red: int
    green: int
    blue: int

    def __getitem__(self, color: str):
        return self.__dict__[color]

    def __setitem__(self, color: str, val):
        self.__dict__[color] = val

    def power(self) -> int:
        return self.red * self.green * self.blue


def checkGameMin(game: str) -> int:
    contents = game.split(";")
    min_colors = dice(red=0, green=0, blue=0)
    for content in contents:
        colors = checkContentMin(content.strip())
        for name, _ in colors.__dict__.items():
            min_colors[name] = max(colors[name], min_colors[name])
    return min_colors.power()


def checkContentMin(content: str) -> dice:
    each = content.split(",")
    colors = dice(red=0, green=0, blue=0)
    for individual in each:
        color = individual.strip().split(" ")
        colors[color[1]] = int(color[0])
    return colors


if __name__ == "__main__":
    games = 0
    with open(input_file, "r") as input:
        for line in input.readlines():
            ln = line.strip()
            if ln == "":
                continue
            name, game = ln.split(":")
            gameID = int(name.split(" ")[1])
            games += checkGameMin(game)
    print(games)

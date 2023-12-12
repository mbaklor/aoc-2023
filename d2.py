input_file = "data-d2"

TARGET_GAME = {"red": 12, "green": 13, "blue": 14}


def checkGameWorks(game: str):
    possible = True
    contents = game.split(";")
    for content in contents:
        possible = possible & checkContentWorks(content.strip())
    return possible


def checkContentWorks(content: str):
    possible = True
    each = content.split(",")
    for individual in each:
        color = individual.strip().split(" ")
        if int(color[0]) > TARGET_GAME[color[1]]:
            possible = False
    return possible


if __name__ == "__main__":
    games = 0
    with open(input_file, "r") as input:
        for line in input.readlines():
            ln = line.strip()
            if ln == "":
                continue
            name, game = ln.split(":")
            gameID = int(name.split(" ")[1])
            if checkGameWorks(game):
                games += gameID
    print(games)

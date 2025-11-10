import requests
from player import Player

def aligned_print(data: list[list[tuple[str, str]]]):
    if len(data) == 0:
        print()
        return

    columns = len(data[0])
    for row in data:
        assert columns == len(row)

    max_column_lengths = [0] * columns
    for row in data:
        for i in range(columns):
            max_column_lengths[i] = max(max_column_lengths[i], len(row[i][1]))

    for row in data:
        for i in range(columns):
            align_dir, string = row[i]
            alignment = max_column_lengths[i] - len(string)

            if i > 0:
                print(" ", end="")

            if align_dir == "right":
                print(" " * alignment, end="")

            print(string, end="")

            if align_dir == "left":
                print(" " * alignment, end="")

        print()

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    finnish_players = [player for player in players if player.nationality == "FIN"]
    finnish_players.sort(key=lambda player: -player.score())

    print("Suomalaiset pelaajat:")

    aligned_print([[
                  ("left", player.name),
                  ("left", " "),
                  ("left", player.team),
                  ("left", " "),
                  ("right", str(player.goals)),
                  ("left", "+"),
                  ("right", str(player.assists)),
                  ("left", "="),
                  ("right", str(player.score()))
              ] for player in finnish_players])

if __name__ == "__main__":
    main()

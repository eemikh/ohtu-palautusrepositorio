from reader import PlayerReader
from stats import PlayerStats

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
    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players")
    stats =PlayerStats(reader)
    finnish_players = stats.top_scorers_by_nationality("FIN")

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

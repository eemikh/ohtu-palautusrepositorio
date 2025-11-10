from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from reader import PlayerReader
from stats import PlayerStats

def main():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
    season = Prompt.ask("Kausi", choices=seasons, default="2024-25")

    reader = PlayerReader(f"https://studies.cs.helsinki.fi/nhlstats/{season}/players")
    stats = PlayerStats(reader)

    nationality = Prompt.ask("Kansallisuus", choices=stats.nationalities)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Pelaajat maasta {nationality}")

    table.add_column("Nimi", justify="left", style="cyan", no_wrap=True)
    table.add_column("Joukkueet", style="magenta")
    table.add_column("Maalit", justify="right", style="green")
    table.add_column("Syötöt", justify="right", style="green")
    table.add_column("Pisteet", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.score()))

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()

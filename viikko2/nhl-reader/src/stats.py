from player import Player
from reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = []
        self.nationalities = []

        for player_dict in reader.read():
            player = Player(player_dict)
            self.players.append(player)

            if player.nationality not in self.nationalities:
                self.nationalities.append(player.nationality)

    def top_scorers_by_nationality(self, nationality: str) -> list[Player]:
        players = [player for player in self.players if player.nationality == nationality]
        players.sort(key=lambda player: -player.score())

        return players

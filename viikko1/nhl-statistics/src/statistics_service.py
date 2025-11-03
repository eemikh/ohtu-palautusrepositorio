from enum import Enum
from player import Player
from player_reader import PlayerReader

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sorting=SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player: Player):
            return player.points

        def sort_by_goals(player: Player):
            return player.goals

        def sort_by_assists(player: Player):
            return player.assists

        sort_keys = {
            SortBy.POINTS: sort_by_points,
            SortBy.GOALS: sort_by_goals,
            SortBy.ASSISTS: sort_by_assists,
        }

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_keys[sorting],
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result

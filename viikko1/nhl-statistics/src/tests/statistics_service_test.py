import unittest
from statistics_service import SortBy, StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_found(self):
        self.assertEqual(self.stats.search("Yzerman").name, "Yzerman")

    def test_search_not_found(self):
        self.assertIsNone(self.stats.search("Me"))

    def test_team(self):
        edm = self.stats.team("EDM")
        edm_player_names = sorted([player.name for player in edm])

        self.assertEqual(edm_player_names, ["Gretzky", "Kurri", "Semenko"])

    def test_top(self):
        top = self.stats.top(2)
        top_player_names = [player.name for player in top]

        self.assertEqual(top_player_names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_goals(self):
        top = self.stats.top(1, sorting=SortBy.GOALS)
        top_player_names = [player.name for player in top]

        self.assertEqual(top_player_names, ["Lemieux", "Yzerman"])

    def test_top_assists(self):
        top = self.stats.top(3, sorting=SortBy.ASSISTS)
        top_player_names = [player.name for player in top]

        self.assertEqual(top_player_names, ["Gretzky", "Yzerman", "Lemieux", "Kurri"])

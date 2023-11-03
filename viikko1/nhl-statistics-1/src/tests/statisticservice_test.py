import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_search_palauttaa_pelaajan(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_palauttaa_none_jos_ei_loydy(self):
        player = self.stats.search("Selanne")
        self.assertEqual(player, None)
    
    def test_team_palauttaa_oikean_maaran_pelaajia(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
    
    def test_team_palauttaa_tyhjan_listan_jos_ei_loydy(self):
        players = self.stats.team("Tappara")
        self.assertEqual(len(players), 0)
    
    def test_top_palauttaa_parhaimman_pelaaan(self):
        players = self.stats.top(1)
        self.assertEqual(players[0].name, "Gretzky")

    def test_top_palauttaa_oikeassa_jarjestyksessa(self):
        players = self.stats.top(3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

    def test_top_palauttaa_oikean_maaran_pelaajia(self):
        players = self.stats.top(3)
        self.assertEqual(len(players), 3)
    
    def test_top_palauttaa_oikeassa_järjestyksessä_maalien_perusteella(self):
        players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Kurri")
    
    def test_top_palauttaa_oikeassa_järjestyksessä_syöttöjen_perusteella(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Lemieux")

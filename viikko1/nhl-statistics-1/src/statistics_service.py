from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by(player, sorting_method=SortBy.POINTS):
    if sorting_method == SortBy.GOALS:
        return player.goals
    elif sorting_method == SortBy.ASSISTS:
        return player.assists
    return player.points

class StatisticsService:
    def __init__(self, io):
        self.io = io
        self._players = self.io.get_players()

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

    def top(self, how_many, sorting_method=SortBy.POINTS):
        
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player:sort_by(player, sorting_method)
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result

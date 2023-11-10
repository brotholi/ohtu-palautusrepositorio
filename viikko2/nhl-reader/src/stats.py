class PlayerStats:

    def __init__(self, io):
        self.io = io
        self._players = self.io.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_players = sorted(self._players, reverse=True, key=lambda player: player.points)

        top_players_by_nationality = []

        for player in top_players:
            if player.nationality == nationality:
                top_players_by_nationality.append(player)
        
        return top_players_by_nationality

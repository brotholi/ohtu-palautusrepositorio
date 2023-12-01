from player import Player
from enum import Enum

class TennisGame:

    class TennisPoints(Enum):
        Love = 0
        Fifteen = 1
        Thirty = 2
        Forty = 3

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name, 0)
        self.player2 = Player(player2_name, 0)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.points += 1
        else:
            self.player2.points += 1

    def get_score(self):
        score = ""
        if self.player1.points == self.player2.points:
            if self.player1.points < 3:  
                score = f"{self.TennisPoints(self.player1.points).name}-All"
            else:
                score = "Deuce"

        else:
            score = self.get_score_when_different()
    
        return score
    
    def get_score_when_different(self):
        score = ""
        if self.player1.points >= 4 or self.player2.points >= 4:
            score = self.get_score_when_advantage()
        else:
            score = f"{self.TennisPoints(self.player1.points).name}-{self.TennisPoints(self.player2.points).name}"
        return score
    
    def get_score_when_advantage(self):
        advancing_player = self.get_advancing_player()

        if abs(self.player1.points - self.player2.points) == 1:
            return f"Advantage {advancing_player.name}"
        else:
            return f"Win for {advancing_player.name}"

    def get_advancing_player(self):
        if self.player1.points > self.player2.points:
            return self.player1
        else:
            return self.player2
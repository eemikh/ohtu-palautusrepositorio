LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = LOVE
        self.m_score2 = LOVE

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return tie_name(self.m_score1)
        elif self.m_score1 > FORTY or self.m_score2 > FORTY:
            return score_name_over_forty(self.m_score1, self.m_score2)
        else:
            return score_name(self.m_score1) + "-" + score_name(self.m_score2)


def tie_name(score):
    if score == LOVE:
        return "Love-All"
    elif score == FIFTEEN:
        return "Fifteen-All"
    elif score == THIRTY:
        return "Thirty-All"
    else:
        return "Deuce"

def score_name(score):
    if score == LOVE:
        return "Love"
    elif score == FIFTEEN:
        return "Fifteen"
    elif score == THIRTY:
        return "Thirty"
    else:
        return "Forty"

def score_name_over_forty(score1, score2):
    assert score1 != score2
    player1_advantage = score1 - score2

    if player1_advantage == 1:
        return "Advantage player1"
    elif player1_advantage == -1:
        return "Advantage player2"
    elif player1_advantage >= 2:
        return "Win for player1"
    else:
        return "Win for player2"

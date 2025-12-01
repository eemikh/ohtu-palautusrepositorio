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
        score = ""

        if self.m_score1 == self.m_score2:
            score = tie_name(self.m_score1)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = score_name(self.m_score1) + "-" + score_name(self.m_score2)

        return score


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

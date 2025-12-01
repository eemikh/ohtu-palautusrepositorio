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
        temp_score = LOVE

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
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == LOVE:
                    score = score + "Love"
                elif temp_score == FIFTEEN:
                    score = score + "Fifteen"
                elif temp_score == THIRTY:
                    score = score + "Thirty"
                elif temp_score == FORTY:
                    score = score + "Forty"

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

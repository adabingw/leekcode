class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        rounds = len(player1)
        score_1 = 0
        score_2 = 0
        for i in range(rounds):
            if i >= 2:
                score_1 += 2 * player1[i] if (player1[i - 1] == 10 or player1[i - 2] == 10) else player1[i]
                score_2 += 2 * player2[i] if (player2[i - 1] == 10 or player2[i - 2] == 10) else player2[i]
            elif i == 1:
                score_1 += 2 * player1[i] if player1[i - 1] == 10 else player1[i]
                score_2 += 2 * player2[i] if player2[i - 1] == 10 else player2[i]
            else:
                score_1 += player1[i]
                score_2 += player2[i]

        if score_1 > score_2:
            return 1
        elif score_2 > score_1:
            return 2

        return 0

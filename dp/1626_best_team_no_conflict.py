class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        dp = [0] * len(scores)
        players = [(ages[i], scores[i]) for i in range(len(scores))] 
        players.sort(key = lambda x: x[0])
        print(players)
        score = 0 
        for i in range(len(scores)): 
            dp[i] = players[i][1] 
            print("dp", dp)
            for j in range(i): 
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
                    print("dp", j, dp)
            score = max(score, dp[i])
        print(dp)
        return score

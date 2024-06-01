class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        game = {}
        for winner, loser in matches:
            if loser not in game:
                game[loser] = 1
            else:
                game[loser] += 1
            
            if winner not in game:
                game[winner] = 0
        
        result = [[], []]
        for player in game:
            if game[player] == 0:
                result[0].append(player)
            elif game[player] == 1:
                result[1].append(player)
        
        result[0].sort()
        result[1].sort()
        
        return result
class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        a = 0 
        b = 0 
        for i in range(1, len(colors) - 1): 
            if colors[i - 1] == colors[i] == colors[i + 1]: 
                if colors[i] == 'A': 
                    a += 1 
                else: 
                    b += 1
        
        return a > b
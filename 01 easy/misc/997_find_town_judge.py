class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusted = [0] * (n + 1)
        print(trusted)

        for a, b in trust: 
            trusted[a] -= 1 
            trusted[b] += 1 
        
        for i in range(1, n + 1): 
            if trusted[i] == n - 1:
                return i 

        return -1 
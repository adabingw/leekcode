class Solution(object):
    def maxConsecutiveAnswers(self, a, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        
        n = len(a)

        def flips(c):
            res = 0
            flip = 0
            l = 0

            for r in range(n):
                if a[r] != c:
                    flip += 1
                if flip > k:
                    while a[l] == c:
                        l += 1
                    l += 1
                    flip -= 1
                
                res = max(res, r - l + 1)
            return res
        
        return max(flips('T'), flips('F'))
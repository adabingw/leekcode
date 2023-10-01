class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        if not s:
            return []
        
        result = []
        
        i = 0
        count = 0

        for j in range(len(s)):
            if s[j] == s[i]:
                count += 1
                if j == len(s) - 1 and count >= 3:
                    result.append([i, j])
            else: 
                if count >= 3:
                    result.append([i, j - 1])
                count = 1
                i = j

        return result    

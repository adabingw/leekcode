class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict) 
        q = [] 
        visited = set() 

        q.append(0) 

        while q: 
            start = q.pop(0) 
            if start in visited: 
                continue 

            for end in range(start + 1, len(s) + 1): 
                if s[start : end] in words: 
                    q.append(end) 
                    if end == len(s):
                        return True 
                visited.add(start) 

        return False
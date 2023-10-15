class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:        
        @lru_cache(None)
        def dp(i):
            pik = []
            
            for j in range(i, n):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if sum(a != b for a, b in zip(words[i], words[j])) == 1:
                        pik = max(pik, dp(j), key = len)
            
            return [words[i]] + pik
        
        return max([dp(i) for i in range(n)], key = len)

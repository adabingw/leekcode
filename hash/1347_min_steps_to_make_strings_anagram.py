class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        freq = defaultdict(int)
        result = 0

        for s1 in s:
            freq[s1] += 1
        
        for t1 in t:
            freq[t1] -= 1
        
        for key in freq:
            result = result + freq[key] if freq[key] > 0 else result
        
        return result
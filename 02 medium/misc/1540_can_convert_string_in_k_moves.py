class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t): 
            return False 

        visited = [] 
        multiplier = defaultdict(lambda: 0)

        for i, j in zip(s, t): 
            swap = ord(j) - ord(i) if (ord(i) <= ord(j)) else 26 - (ord(i) - ord(j))
            print(swap)
            if swap == 0: 
                continue 

            if swap + multiplier[swap] * 26 <= k: 
                multiplier[swap] += 1 
            elif swap + multiplier[swap] * 26 > k: 
                return False 

        return True 
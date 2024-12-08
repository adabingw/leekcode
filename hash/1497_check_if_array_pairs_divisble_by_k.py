class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        freq = Counter()

        for a in arr:
            target = ((a % k) + k) % k
            freq[target] += 1
        
        for i in range(k):
            if i == 0:
                if freq[i] % 2 != 0:
                    return False
            
            else:
                if freq[i] != freq[k - i]:
                    return False
        
        return True
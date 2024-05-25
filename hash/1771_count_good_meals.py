class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m = defaultdict(int)
        result = 0

        for delicious in deliciousness:
            for i in range(22):
                result = (result + m[(2 ** i) - delicious])
        
            m[delicious] += 1
        
        return result % MOD
class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        dp = [1] + [0] * (n - 1) 

        start, end = 0, 1
        for i in range(delay, n):
            # nobody forgets anything yet 
            if i < forget - 1:
                dp[i] = sum(dp[:end])
                end += 1
            else:
                dp[i] = sum(dp[start:end])
                end += 1
                start += 1

        return sum(dp[n-forget:]) % (10**9 + 7)
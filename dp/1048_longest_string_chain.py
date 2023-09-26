class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(lambda x,y: cmp(len(x), len(y)))

        result = 0
        dp = defaultdict(int)
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                dp[word] = max(dp[prev] + 1, dp[word])
                result = max(result, dp[word])
        return result

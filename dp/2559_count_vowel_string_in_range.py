class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dp = [0]
        ans = []
        s = 0
        for word in words: 
            if word[0] in 'aeiou' and word[-1] in 'aeiou': 
                s += 1 
            dp.append(s)
                 
        for start, end in queries: 
            ans.append(dp[end + 1] - dp[start])
        print(ans)
        return ans
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # maxf -> max frequency of same character in sliding window
        # or max(count.values())
        maxf = res = 0
        count = collections.Counter()

        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])

            # replacement cost: cell count between left and right pointers - highest frequency
            
            # replacement cost is less than k
            if res - maxf < k:
                # increase window size
                res += 1
            else:
                # decrease frequency of character at left pointer
                # don't need to shrink window because we're finding longest substr
                # we just continue sliding until we find a window with a larger size
                count[s[i - res]] -= 1
        return res

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        res = 0

        freq = [0] * 3

        while right < len(s):
            freq[ord(s[right]) - ord("a")] += 1

            while all(f > 0 for f in freq):
                res += len(s) - right
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1
            right += 1

        return res
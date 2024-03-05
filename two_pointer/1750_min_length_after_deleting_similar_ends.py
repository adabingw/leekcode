class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s) - 1

        while left < right:
            print(left, right)
            if s[left] != s[right]:
                break

            while left < len(s) - 1 and s[left] == s[left + 1]:
                left += 1

            while right > 0 and s[right] == s[right - 1]:
                right -= 1

            left += 1
            right -= 1
            
        return right - left + 1 if right - left >= 0 else 0
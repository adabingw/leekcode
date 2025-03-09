class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        for i in range(k - 1):
            colors.append(colors[i])

        n = len(colors)
        res = 0
        left = 0
        right = 1

        while right < n:
            if colors[right] == colors[right - 1]:

                # Pattern breaks, reset window from the current position
                left = right
                right += 1
                continue

            # Extend window
            right += 1

            # Skip counting sequence if its length is less than k
            if right - left < k:
                continue

            # Record a valid sequence and shrink window from the left to search for more
            res += 1
            left += 1

        return res
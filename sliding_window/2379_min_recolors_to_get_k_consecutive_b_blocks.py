class Solution:
    def minimumRecolors(self, blocks, k):
        left = 0
        num_whites = 0
        res = float("inf")

        for right in range(len(blocks)):

            if blocks[right] == "W":
                num_whites += 1

            if right - left + 1 == k:

                res = min(res, num_whites)
                if blocks[left] == "W":
                    num_whites -= 1

                left += 1

        return res
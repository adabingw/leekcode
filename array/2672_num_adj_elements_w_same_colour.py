class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums = [0] * n
        result = [0] * len(queries)
        count = 0

        for i, (index, colour) in enumerate(queries):
            left = nums[index - 1] if index > 0 else 0
            right = nums[index + 1] if index < n - 1 else 0
            if nums[index] != 0 and nums[index] == left:
                count -= 1
            if nums[index] != 0 and nums[index] == right:
                count -= 1
            if colour == left:
                count += 1
            if colour == right:
                count += 1
            nums[index] = colour
            result[i] = count
            
        return result

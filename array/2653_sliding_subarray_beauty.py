class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        n = len(nums)
        if n < k:
            return []

        result = []
        d = {i: 0 for i in range(-50, 0)}

        for i, v in enumerate(nums):
            if v < 0:
                d[v] += 1

            if i >= k:
                if nums[i - k] < 0:
                    d[nums[i - k]] -= 1

            if i >= k - 1:
                count = 0
                for index in range(-50, 0, 1):
                    value = d[index]
                    count += value
                    if count >= x:
                        result.append(index)
                        break
                
                if count < x:
                    result.append(0)
        
        return result

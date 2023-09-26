class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        arr = sorted([num, c] for num, c in zip(nums, cost))
        prefix = [0] * len(nums) 
        prefix[0] = arr[0][1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + arr[i][1]
        
        result = 0
        cost = 0
        for i in range(1, len(nums)):
            cost += arr[i][1] * (arr[i][0] - arr[0][0])
        result = cost

        for i in range(1, len(nums)):
            diff = arr[i][0] - arr[i - 1][0]
            cost += diff * prefix[i - 1]
            cost -= diff * (prefix[-1] - prefix[i - 1])
            result = min(result, cost)

        return result

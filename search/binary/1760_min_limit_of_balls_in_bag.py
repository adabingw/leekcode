class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """

        def is_possible(m):
            ops = 0
            for num in nums:

                # num ops to split this bag
                operations = (num - 1) // m
                ops += operations

                if ops > maxOperations:
                    return False
            
            return True
        
        left = 1
        right = max(nums)

        while left < right:
            middle = (left + right) // 2

            if is_possible(middle):
                right = middle
            else:
                left = middle + 1
        
        return left
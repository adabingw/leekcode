class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        zero = 0

        while zero < len(nums) and nums[zero] < 0:
            zero += 1
        
        left = zero - 1

        while left >= 0:
            if zero < len(nums) - 1 and nums[zero] <= nums[zero + 1] < abs(nums[left]):
                zero += 1
                continue
            if 0 < zero < len(nums) and abs(nums[left]) < nums[zero]:
                nums.insert(zero, abs(nums[left]))
                nums.pop(left)
            else:
                nums.insert(zero + 1, abs(nums[left]))
                nums.pop(left)
            left -= 1

        result = []
        for num in nums:
            result.append(num * num)

        
        return result

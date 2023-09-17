class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        latest = -101
        for index, num in enumerate(nums): 
            if latest == num: 
                while nums[index] == latest: 
                    nums.pop(index) 
                    if index == len(nums): 
                        return len(nums)
            latest = nums[index]
        print(nums) 
        return len(nums)
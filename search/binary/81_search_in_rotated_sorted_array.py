class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 1:
            return nums[0] == target
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            elif nums[left] <= nums[mid]:

                # target in between left and mid
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else: # nums[mid] < target
                    left = mid + 1
            
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
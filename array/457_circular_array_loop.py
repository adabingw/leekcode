class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2: 
            return False 
        
        n = len(nums) 
        for i in range(n): 
            visited = [] 
            direction = (nums[i] > 0)
            while (i not in visited) and (direction ^ (nums[i] < 0)) and (nums[i] % n != 0): 
                visited.append(i) 
                next_node = nums[i] 
                i = (i + next_node) % n 
            
            if i in visited: 
                return True 
        return False 

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res = ""
        for i in range(len(nums)):
            curr = nums[i][i]
            res += "1" if curr == "0" else "0"
        
        return res
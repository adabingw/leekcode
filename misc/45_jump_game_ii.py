class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0

        curr_end, curr_far = 0, 0

        for i, n in enumerate(nums): 
            if i == len(nums) - 1: 
                return answer 

            curr_far = max(curr_far, i + n)
            if i == curr_end: 
                answer += 1 
                curr_end = curr_far

        return answer

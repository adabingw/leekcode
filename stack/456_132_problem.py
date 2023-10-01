class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        # min_list = [0] * n
        # for i in range(n):
        #     min_list[i] = min(nums[:i + 1])
        min_list = list(accumulate(nums, min))
        
        stack = []
        n = len(nums)

        for i in range(n - 1, -1, -1):
            if nums[i] > min_list[i]:
                while stack and stack[-1] <= min_list[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        
        return False

class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(nums) < k:
            return 0

        result = 0
        curr_sum = 0
        right = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            new_element = nums[right]
            freq[new_element] += 1
            curr_sum += new_element

            if right >= k:
                exit_element = nums[right - k]
                freq[exit_element] -= 1
                if freq[exit_element] == 0:
                    del freq[exit_element]
                
                curr_sum -= exit_element

            if len(freq) >= m:
                result = max(result, curr_sum)

        return result

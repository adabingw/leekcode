class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        result = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for k in freq:
            if freq[k] > math.floor(n / 3):
                result.append(k)
        return result

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = defaultdict(int)
        result = 0
        for num in nums:
            freq[num] += 1
        print(freq)
        for i in freq.keys():
            if freq[i] == 1:
                return -1
            elif freq[i] % 3 == 0:
                result += freq[i] / 3
            elif freq[i] == 2:
                result += 1
            elif freq[i] == 4:
                result += 2
            else:
                if (freq[i] - 4) % 3 == 0:
                    result += 2
                    result += (freq[i] - 4) / 3
                elif (freq[i] - 2) % 3 == 0:
                    result += 1
                    result += (freq[i] - 2) / 3
        return result
        
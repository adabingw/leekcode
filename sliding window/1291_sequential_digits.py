class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        nums = '123456789'
        result = []

        for wsize in range(len(str(low)), len(str(high)) + 1):
            l = 0
            currnum = [nums[l]]
            for right in range(1, len(nums)):
                if int(''.join(currnum)) > high:
                    break
                if len(currnum) == wsize:
                    if (int(''.join(currnum)) >= low):
                        result.append(int(''.join(currnum)))
                    currnum.pop(0)
                    l += 1
                currnum.append(nums[right])
            if len(currnum) == wsize and low <= int(''.join(currnum)) <= high:
                result.append(int(''.join(currnum)))
        return result

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        prev_max = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = prev_max
            prev_max = max(prev_max, temp)
        
        return arr

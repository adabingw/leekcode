class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        # so that we don't need to divide our avg
        thres = k * threshold
        result = 0
        curr_sum = 0

        for i, a in enumerate(arr):
            if i >= k:
                if curr_sum >= thres:
                    result += 1
                out = arr[i - k]
                curr_sum -= out
                curr_sum += a
            else:
                curr_sum += a
        
        if curr_sum >= thres:
                    result += 1
        
        return result

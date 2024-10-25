class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0

        n = len(arr)
        res = 0
        base = 0

        while base < n:
            end = base

            # if base is left-boundary
            if end + 1 < n and arr[end] < arr[end + 1]:

                # set end to the peak of potential mountain
                while end + 1 < n and arr[end] < arr[end + 1]:
                    end += 1
                
                # if end is really a peak
                if end + 1 < n and arr[end] > arr[end + 1]:

                    # set end to right boundary of mountain
                    while end + 1 < n and arr[end] > arr[end + 1]:
                        end += 1
                    
                    res = max(res, end - base + 1)
            
            base = max(end, base + 1)
        
        return res
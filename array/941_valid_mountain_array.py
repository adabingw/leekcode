class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False 

        decreasing = False
        increasing = False
        for i in range(len(arr) - 1):
            if arr[i + 1] == arr[i]:
                return False

            if decreasing:
                if arr[i + 1] > arr[i]:
                    return False
            else: 
                if arr[i + 1] < arr[i]:
                    if not increasing:
                        return False
                    decreasing = True
                else: 
                    increasing = True
        
        if not decreasing:
            return False

        return True

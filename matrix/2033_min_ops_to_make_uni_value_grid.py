class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for g in grid:
            arr = arr + g

        if len(arr) == 1:
            return 0

        arr.sort()
        med1 = arr[len(arr) // 2]
        med2 = arr[len(arr) // 2 - 1]

        res1 = 0
        res2 = 0
        for a in arr:
            if abs(a - med1) % x != 0:
                res1 = -1
                break
            else:
                res1 += (abs(a - med1) / x)
            
            if abs(a - med2) % x != 0:
                res2 = -1
                break
            else:
                res2 += (abs(a - med2) / x)
        
        return min(int(res1), int(res2))
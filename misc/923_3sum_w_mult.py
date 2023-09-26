class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        if len(arr) < 3:
            return 0
        
        arr = sorted(arr)
        result = 0

        for i, a in enumerate(arr):
            remaining = target - a
            j = i + 1
            k = len(arr) - 1
            while (j < k):
                if arr[j] + arr[k] == remaining:
                    # different cases
                    if arr[j] == arr[k]:
                        result += (k - j + 1) * (k - j) / 2
                        result %= 10 ** 9 + 7
                        break
                    else:
                        j_freq = 1
                        k_freq = 1

                        # compiling the duplicates
                        while arr[j + 1] == arr[j]:
                            j_freq += 1
                            j += 1
                        while arr[k - 1] == arr[k]: 
                            k_freq += 1
                            k -= 1

                        result += j_freq * k_freq
                        result %= 10 ** 9 + 7
                        j += 1
                        k -= 1
                elif arr[j] + arr[k] < remaining:
                    j += 1
                else:
                    k -= 1
        
        return result

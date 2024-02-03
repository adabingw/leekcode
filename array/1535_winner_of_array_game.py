class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        win_count = 0
        winner = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                win_count = 0
            win_count += 1
            if win_count == k:
                break

        return winner

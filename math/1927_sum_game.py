class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        left_q, right_q = 0, 0
        left_sum, right_sum = 0, 0
        for i in range(len(num) // 2):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
        for i in range(len(num) // 2, len(num)):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        
        qmarks_diff = right_q - left_q
        sum_diff = left_sum - right_sum
        return qmarks_diff % 2 == 1 or qmarks_diff // 2 * 9 != sum_diff
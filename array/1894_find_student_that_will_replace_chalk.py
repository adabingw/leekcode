class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        m = sum(chalk)
        k = k % m

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            else:
                k -= chalk[i]
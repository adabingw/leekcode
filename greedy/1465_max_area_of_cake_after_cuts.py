class Solution(object):
    def maxArea(self, h, w, hc, vc):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        hc.sort()
        vc.sort()

        MOD = 10 ** 9 + 7

        hc.append(h)
        vc.append(w)
        max_h = hc[0]
        max_v = vc[0]

        for i in range(0, len(hc) - 1):
            max_h = max(max_h, hc[i + 1] - hc[i])
        for i in range(0, len(vc) - 1):
            max_v = max(max_v, vc[i + 1] - vc[i])
        
        return (max_h * max_v) % MOD
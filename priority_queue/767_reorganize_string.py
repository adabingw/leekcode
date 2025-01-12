class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        d = Counter(s)

        h = []

        for i in d:
            heappush(h, (-d[i], i))
        
        # so that we don't add immediately into heap
        # store it to add after a loop
        p_i = 0
        p_j = ''

        res = ''

        while h:
            i, j = heappop(h)
            res += j

            if p_i < 0:
                heapq.heappush(h, (p_i, p_j))
            
            i += 1
            p_i = i
            p_j = j

        return res if len(res) == len(s) else ''
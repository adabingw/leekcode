class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        m = defaultdict(int)
        for u, v in roads:
            m[u] += 1
            m[v] += 1
        
        a = []
        for k in m:
            a.append((k, m[k]))
        a = sorted(a, key=lambda x: x[1], reverse=True)
        
        for r, r1 in a:
            m[r] = n
            n -= 1
        
        result = 0
        for u, v in roads:
            result += (m[u] + m[v])

        return result
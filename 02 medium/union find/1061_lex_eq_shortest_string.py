class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """

        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX > rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
        
        # Union the two equivalent characters
        # at the same position from s1 and s2 into the same group.
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        res = ""
        for c in baseStr:
            res += find(c)
            
        return res 
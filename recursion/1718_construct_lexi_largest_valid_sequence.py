class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n * 2 - 1)
        used = set()

        def find_seq(i):
            if i == len(res):
                return True
            
            if res[i] != 0:
                return find_seq(i + 1)

            for j in range(n, 0, -1):
                if j in used:
                    continue
                
                used.add(j)
                res[i] = j

                if j == 1:
                    if find_seq(i + 1):
                        return True
                elif i + j < len(res) and res[i + j] == 0:
                    res[i + j] = j
                
                    if find_seq(i + 1):
                        return True
                    
                    res[i + j] = 0
            
                res[i] = 0
                used.remove(j)

            return False

        find_seq(0)
        return res
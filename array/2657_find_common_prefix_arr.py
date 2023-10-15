class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = [0] * len(A)
        a_ = [A[0]]
        b_ = [B[0]]
        result[0] = 1 if A[0] == B[0] else 0

        for i in range(1, len(A)):
            a_.append(A[i])
            b_.append(B[i])
            this_common = 0
            if A[i] in b_:
                this_common += 1
            if B[i] in a_:
                this_common += 1
            
            if A[i] == B[i]:
                this_common = 1
            
            result[i] = result[i - 1] + this_common
        
        return result

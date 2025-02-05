class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c1 = None
        c2 = None
        flag = False

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if c1 == None and c2 == None and not flag:
                    c1 = s1[i]
                    c2 = s2[i]
                elif s1[i] == c2 and s2[i] == c1 and not flag:
                    flag = True

                else:
                    return False

        # c1 == c2 == None means all chars same
        # flag == True means all swaps have been swapped
        return (c1 == c2 == None) or (flag)
        

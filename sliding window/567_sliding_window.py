class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        s2_hash = defaultdict(int)
        s1_hash = defaultdict(int)

        for s in s1:
            s1_hash[str(s)] += 1
        
        wsize = len(s1)

        for right in range(len(s2)):
            if right >= wsize:
                if s2_hash == s1_hash:
                    return True
                s2_hash[str(s2[right - wsize])] -= 1
                if s2_hash[str(s2[right - wsize])] == 0:
                    del s2_hash[str(s2[right - wsize])]
            s2_hash[str(s2[right])] += 1
        
        if s2_hash == s1_hash:
            return True

        return False

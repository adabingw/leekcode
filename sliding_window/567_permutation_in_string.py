class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_counter[s2[right]] += 1
            s2_counter[s2[left]] -= 1

            if s2_counter[s2[left]] == 0:
                del s2_counter[s2[left]]
            
            left += 1

            if s1_counter == s2_counter:
                return True
        
        return False
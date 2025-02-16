class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """

        if len(s) == 1 and k == 1:
            return True
        if len(s) < k:
            return False

        curr_char = s[0]
        char_count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:  
                char_count += 1
            else:
                if char_count == k:
                    return True
                
                curr_char = s[i]
                char_count = 1

        if char_count == k:
            return True
    
        return False
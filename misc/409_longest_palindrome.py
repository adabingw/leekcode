class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = {}
        for i in s: 
            if str(i) in alphabet: 
                alphabet[str(i)] = alphabet[str(i)] + 1 
            else: 
                alphabet[str(i)] = 1

        if len(alphabet) == 1: 
            for key in alphabet: return alphabet[key]
        
        odds = False 
        res = 0
        for key in alphabet: 
            if alphabet[key] % 2 is not 0: 
                odds = True 
                res = res + alphabet[key] - 1
            elif alphabet[key] % 2 == 0: 
                res = res + alphabet[key]
        
        if odds: 
            res = res + 1 

        return res
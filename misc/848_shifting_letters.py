class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        result = []
        x = sum(shifts) % 26
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            result.append(chr(ord('a') + (index + x) % 26))
            x = (x - shifts[i]) % 26
        
        return ''.join(result)

class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = 0

        for i in range(0, len(word)):
            if i == 0:
                result += ord(word[i]) - ord('a')
            elif ord(word[i]) - ord(word[i - 1]) == 2:
                result += 1
            elif ord(word[i]) - ord(word[i - 1]) == 1:
                continue
            elif ord(word[i]) - ord(word[i - 1]) == -1:
                result += 1
            elif word[i] == word[i - 1]: 
                result += 2
        
        result += ord('c') - ord(word[-1])

        return result

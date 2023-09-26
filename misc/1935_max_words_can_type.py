class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split(' ')
        result = len(words)

        for word in words:
            for letter in brokenLetters:
                if letter in word:
                    result -= 1
                    break
        
        return result

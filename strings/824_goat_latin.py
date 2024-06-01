class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = defaultdict(bool)
        vowels['a'] = True
        vowels['e'] = True
        vowels['i'] = True
        vowels['o'] = True
        vowels['u'] = True
        words = sentence.split(' ')

        for index, word in enumerate(words):
            if vowels[str(word[0].lower())]:
                word += 'ma'
            else:
                word = word[1:] + word[0]
                word += 'ma'
            
            word += 'a' * (index + 1)
            words[index] = word

        return ' '.join(words)
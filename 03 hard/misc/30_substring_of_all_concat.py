class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        k = len(words)
        word_length = len(words[0]) 
        substring_length = word_length * k
        word_count = collections.Counter(words) 

        def check(i): 
            remaining = copy.deepcopy(word_count)
            matches = 0 

            for j in range(i, i + substring_length, word_length): 
                segment = s[j : j + word_length]
                if remaining[segment] > 0: 
                    remaining[segment] -= 1 
                    matches += 1
                else:
                    break
            return matches == k
        
        result = []
        for i in range(n - substring_length + 1): 
            if check(i): 
                result.append(i)

        return result
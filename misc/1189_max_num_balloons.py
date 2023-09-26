class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = defaultdict(int)
        for t in text:
            freq[t] += 1
        
        result = float('inf')
        for letter in ['b', 'a', 'l', 'o', 'n']:
            if letter == 'b' or letter == 'a' or letter == 'n':
                result = min(result, freq[letter])
            else:
                result = min(result, freq[letter] // 2)
        
        return result

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        freq = {}
        visited_freq = []

        for i in s:
            if i in freq:
                freq[str(i)] += 1
            else: 
                freq[str(i)] = 1

        for char in freq.keys():
            f = freq[char]
            print(f, visited_freq)
            if f in visited_freq:
                while f in visited_freq and f != 0:
                    f -= 1
                    result += 1
            if f > 0:
                visited_freq.append(f)

        return result

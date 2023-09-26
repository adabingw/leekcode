class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """

        if minSize > len(s):
            return 0
        
        result = 0
        dic = defaultdict(int)
        curr = []

        for i, c in enumerate(s):
            if len(curr) == minSize:
                old_letter = curr.pop(0)
                curr.append(str(c))
            else:
                curr.append(str(c))
                
            if len(curr) == minSize:
                if len(set(curr)) <= maxLetters:
                    curr_str = ''.join(curr)
                    dic[curr_str] += 1
                    result = max(dic[curr_str], result)
        
        return result

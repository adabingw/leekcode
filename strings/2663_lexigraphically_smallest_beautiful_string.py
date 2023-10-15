class Solution(object):
    def smallestBeautifulString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        # string u r given is already beautiful
        # no palindromes in string

        sl = list(s)
        i = len(s) - 1

        sl[i] = chr(ord(s[i]) + 1)

        while 0 <= i < len(s):
            if ord(sl[i]) - ord('a') >= k:
                sl[i] = 'a'
                i -= 1
                sl[i] = chr(ord(sl[i]) + 1)
            elif (i >= 1 and sl[i] == sl[i - 1]) or (i >= 2 and sl[i] == sl[i - 2]):
                sl[i] = chr(ord(sl[i]) + 1)
            else:
                i += 1

        return '' if i < 0 else ''.join(sl)

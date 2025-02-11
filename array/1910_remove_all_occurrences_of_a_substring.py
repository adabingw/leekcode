class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        
        while part in s:
            part_start_index = s.find(part)
            s = s[:part_start_index] + s[part_start_index + len(part) :]

        return s
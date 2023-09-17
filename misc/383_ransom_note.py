class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote: 
            if i in magazine: 
                magazine = magazine[:magazine.find(i)] + magazine[magazine.find(i) + 1:]
            else:
                return False
        return True 
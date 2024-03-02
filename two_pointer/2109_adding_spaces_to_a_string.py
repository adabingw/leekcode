class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        s = list(s)
        ind = 0
        
        for i, s1 in enumerate(s):
            if ind < len(spaces) and i == spaces[ind]:
                result += " "
                ind += 1
            result += str(s1)
        return result
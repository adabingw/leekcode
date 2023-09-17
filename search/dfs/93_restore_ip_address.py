class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        result = []

        def dfs(s, index, path): 
            if index > 4: 
                return 
            if index == 4 and not s: 
                result.append(path[:-1])
            
            for i in range(1, len(s) + 1): 
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256): 
                    dfs(s[i:], index + 1, path + s[:i] + '.')

        dfs(s, 0, "")
        return result
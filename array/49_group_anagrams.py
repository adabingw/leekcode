class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        a_map = defaultdict(list)

        for s in strs:
            a_map["".join(sorted(s))].append(s)
        
        for k in a_map:
            result.append(a_map[k])
        
        return result

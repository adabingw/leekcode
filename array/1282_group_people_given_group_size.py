class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        result = []
        groups = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] == 1:
                result.append([ i ])
            elif groupSizes[i] in groups.keys():
                groups[groupSizes[i]].append(i)
                if len(groups[groupSizes[i]]) == groupSizes[i]:
                    result.append(groups[groupSizes[i]])
                    groups[groupSizes[i]] = []
            else:
                groups[groupSizes[i]] = [ i ]
        return result

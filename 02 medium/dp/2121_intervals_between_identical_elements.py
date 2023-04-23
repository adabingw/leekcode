class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        elements = defaultdict(list) 
        for index, a in enumerate(arr): 
            elements[a].append(index) 

        res = [0] * len(arr)
        for element, indices in elements.items(): 
            pre = [0] * (len(indices) + 1) 
            for index in range(len(indices)): 
                pre[index + 1] = pre[index] + indices[index]
            for i, index in enumerate(indices): 
                res[index] = (index * (i + 1) - pre[i + 1]) \
                            + ((pre[len(indices)] - pre[i]) - index * (len(indices) - (i)))
        print(res)
        return res
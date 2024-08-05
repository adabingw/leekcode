class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        
        arr_count = Counter(arr)
        distinct = []

        for a in arr:
            if arr_count[a] == 1:
                distinct.append(a)
        
        return distinct[k - 1] if k <= len(distinct) else ""
        
        

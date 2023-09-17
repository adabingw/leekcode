class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        query = [] 
        for n1 in nums1: 
            index = nums2.index(n1) 
            arr = nums2[index: ]
            j = 0
            while arr and arr[j] <= n1: 
                arr.pop(0) 
            if arr: 
                query.append(arr[0]) 
            else: 
                query.append(-1) 
        return query
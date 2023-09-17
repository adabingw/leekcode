# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def bst(nums): 
            if not nums: 
                return None 
                
            mid = len(nums) / 2 
            print(mid, nums)

            node = TreeNode(nums[mid]) 

            node.left = bst(nums[:mid]) 
            node.right = bst(nums[mid + 1:]) 

            return node
        
        return bst(nums)
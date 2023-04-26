# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, low=-float("inf"), high=float("inf")):
            if not node: 
                return True 

            if node.val <= low or node.val >= high: 
                return False
            
            return valid(node.right, node.val, high) and valid(node.left, low, node.val) 
        
        return valid(root)
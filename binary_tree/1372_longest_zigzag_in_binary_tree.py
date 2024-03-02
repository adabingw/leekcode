# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.path = 0 

        def dfs(node, left, curr): 
            if node is None: 
                return 
            else: 
                self.path = max(self.path, curr) 
                if left: 
                    dfs(node.left, False, curr + 1)
                    dfs(node.right, True, 1)
                elif not left: 
                    dfs(node.left, False, 1) 
                    dfs(node.right, True, curr + 1) 
        
        dfs(root, False, 0) 
        dfs(root, True, 0)
        return self.path
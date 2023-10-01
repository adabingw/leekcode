# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if not root: 
            return False

        def dfs(node, path_sum): 
            if not node: 
                return False 

            path_sum += node.val

            if node.left is None and node.right is None: 
                if path_sum == targetSum: 
                    return True
                
            return dfs(node.left, path_sum) or dfs(node.right, path_sum)
            

        return dfs(root, 0)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        def dfs(node, parent, depth, mod): 
            if node: 
                if node.val == mod: 
                    return depth, parent
                return dfs(node.left, node, depth + 1, mod) or dfs(node.right, node, depth + 1, mod) 
            
        dx, px, dy, py = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return dx == dy and px != py
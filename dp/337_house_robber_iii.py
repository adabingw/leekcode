# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def robrob(node):
            if not node:
                return (0, 0)
            
            robleft = robrob(node.left)
            robright = robrob(node.right)

            robnow = node.val + robleft[1] + robright[1]

            roblater = max(robleft) + max(robright)

            return (robnow, roblater)
        
        return max(robrob(root))
            
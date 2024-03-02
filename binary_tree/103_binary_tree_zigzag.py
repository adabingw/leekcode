# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        q = [root] 
        result = []
        direction = 1

        while q: 
            level = []
            for i in range(len(q)): 
                node = q.pop(0) 
                level.append(node.val) 
                if node.left: 
                    q.append(node.left) 
                if node.right: 
                    q.append(node.right)
            result.append(level[::direction]) 
            direction *= (-1)

        return result
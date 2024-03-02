# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        width = 0
        q = [(1, root)]
        while q:
            width = max(width, q[-1][0] - q[0][0] + 1)
            count = len(q)
            for i in range(count): 
                index, node = q.pop(0) 
                for child in enumerate((node.left, node.right), 2 * index): 
                    if child[1]: 
                        q.append(child)
        return width
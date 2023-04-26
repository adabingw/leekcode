# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        q = [] 
        result = [] 

        if root: 
            q.append(root) 
        
        while q: 
            level = [] 
            n = len(q) 

            for _ in range(n): 
                node = q.pop(0) 
                level.append(node.val) 

                if node.left: 
                    q.append(node.left) 

                if node.right: 
                    q.append(node.right) 
            
            result.append(level) 
        
        return result[::-1]
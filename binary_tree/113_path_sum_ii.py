# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        if not root: 
            return []

        self.result = []

        def dfs(node, path):
            if not node: 
                return 

            path.append(node.val)

            if node.left is None and node.right is None: 
                if sum(path) == targetSum: 
                    self.result.append(copy.deepcopy(path))
            else:
                dfs(node.left, path) 
                dfs(node.right, path)

            path.pop()

        dfs(root, [])

        return self.result
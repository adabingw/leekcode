# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        self.visited = set()

        def dfs(node, value):
            if not node:
                return

            self.visited.add(value)
            dfs(node.left, value * 2 + 1)
            dfs(node.right, value * 2 + 2)

        dfs(root, 0)

    def find(self, target):
        return target in self.visited
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        g = defaultdict(list)
        
        def constructGraph(node, parent):
            if not node:
                return
            
            if parent:
                g[parent.val].append(node.val)
                g[node.val].append(parent.val)
            constructGraph(node.left, node)
            constructGraph(node.right, node)
        
        constructGraph(root, None)
        visited = defaultdict(bool)
        
        def dfs(node, res):
            if not node:
                return res
            
            ans = res
            for v in g[node]:
                if not visited[v]:
                    visited[v] = True
                    ans = max(ans, dfs(v, res + 1))
            return ans
        
        visited[start] = True
        result = dfs(start, 0)

        return result
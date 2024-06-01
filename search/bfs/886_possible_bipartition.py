class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        groups = {}

        for i in range(n):

            if i in groups:
                continue
            
            groups[i] = 1
            queue = [(i, 1)]

            while queue:
                person, group = queue.pop(0)
                for dislike in adj[person]:

                    if dislike not in groups:
                        groups[dislike] = 1 if group == 0 else 0
                        queue.append((dislike, groups[dislike]))
                    elif groups[dislike] == group:
                        return False
            
        return True
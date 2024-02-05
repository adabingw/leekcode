class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        global prereqs, visited
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        visited = [False] * numCourses

        def dfs(course):
            global prereqs, visited
            visited[course] = True
            for c in prereqs[course]:
                if visited[c]:
                    return True
            for c in prereqs[course]:
                if not visited[c]:
                    res = dfs(c)
                    visited[course] = False
                    return res
            visited[course] = False
            return False

        for a in prereqs.keys():
            has_cycle = dfs(a)
            if has_cycle:
                return False
        return True

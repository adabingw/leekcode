class Solution(object):
    def findOrder(self, N, P):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        G, indegree, ans = defaultdict(list), [0] * N, []
        for course, pre in P:
            G[pre].append(course)
            indegree[course] += 1
        
        def dfs(course):
            ans.append(course)
            indegree[course] = -1
            for nextCourse in G[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0: 
                    dfs(nextCourse)         
                       
        for i in range(N):
            if indegree[i] == 0:
                dfs(i)

        return ans if len(ans) == N else []

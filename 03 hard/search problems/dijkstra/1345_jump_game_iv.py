import collections 

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 1: return 0 

        d = collections.defaultdict(list)
        n = len(arr)
        dq = deque([(0, 0)]) 
        visited = set()

        for i, num in enumerate(arr):
            d[num].append(i)
        print(d)

        while dq:
            steps, index = dq.popleft()
            if index == n - 1: # found last node 
                return steps
            
            for neighbour in [index - 1, index + 1]:
                if 0 <= neighbour < n and neighbour not in visited:
                    # not visited, we visit it by adding a step
                    visited.add(neighbour)
                    dq.append((steps + 1, neighbour))
            
            # add the nodes with same value also in the deque and in the visited
            if d[arr[index]]:
                for node in d[arr[index]]:
                    if node not in visited:
                        visited.add(node)
                        dq.append((steps + 1, node))
                d[arr[index]] = []
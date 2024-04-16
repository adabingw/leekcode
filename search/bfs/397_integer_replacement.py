class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        visited = {}
        q = [[n, 0]]

        while q:
            num, ops = q.pop(0)
            if num == 1:
                return ops
            if num % 2 == 0 and not num / 2 in visited:
                q.append([num / 2, ops + 1])
            if num % 2 != 0 and not num + 1 in visited:
                q.append([num + 1, ops + 1])
            if num % 2 != 0 and num != 0 and not num - 1 in visited:
                q.append([num - 1, ops + 1])
            visited[num] = True

        return 0
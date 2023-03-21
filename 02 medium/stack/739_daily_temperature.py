class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures): 
            while stack and temperatures[stack[-1]] < temperature: 
                cur = stack.pop()
                ans[cur] = index - cur
            stack.append(index)

        return ans
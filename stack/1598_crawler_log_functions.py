class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        operations = [] 
        for log in logs: 
            if operations and '../' in log: 
                operations.pop()
            elif './' in log: 
                continue 
            else: 
                operations.append(log)
        return len(operations)
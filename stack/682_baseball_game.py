class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        while operations: 
            op = operations.pop(0)
            if op == '+': 
                score.insert(0, score[0] + score[1])
            elif op == 'D': 
                score.insert(0, 2 * score[0]) 
            elif op == 'C': 
                score.pop(0)
            else: 
                score.insert(0, int(op))
        return sum(score)
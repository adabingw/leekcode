class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        result = 0
        for i, v in enumerate(rating[1:-1]):
            left_less, left_greater, right_less, right_greater = 0, 0, 0, 0
            for left in rating[:i+1]:
                if left < v:
                    left_less += 1
                elif left > v:
                    left_greater += 1
            for right in rating[i+2:]:
                if right > v:
                    right_greater += 1
                elif right < v:
                    right_less += 1
            result += left_less * right_greater + left_greater * right_less
        return result

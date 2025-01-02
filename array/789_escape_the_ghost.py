class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        target_distance = abs(target[0]) + abs(target[1])
        for i, j in ghosts:
            if abs(target[0] - i) + abs(target[1] - j) <= target_distance:
                return False
        
        return True
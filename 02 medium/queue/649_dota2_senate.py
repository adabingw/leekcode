import collections 

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate_deque = collections.deque()
        senators = [0, 0]
        bans = [0, 0]

        for senator in senate:
            x = 1 if senator == 'R' else 0
            senators[x] += 1
            senate_deque.append(x)

        # The all() function returns True if all elements in the given iterable are true. 
        # If not, it returns False
        while all(senators):
            x = senate_deque.popleft()
            senators[x] -= 1
            if bans[x]:
                bans[x] -= 1
            else:
                bans[x^1] += 1
                senate_deque.append(x)
                senators[x] += 1

        return "Radiant" if senators[1] else "Dire"
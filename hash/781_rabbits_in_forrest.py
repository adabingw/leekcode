class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        rabbits = defaultdict(int)
        result = 0

        # x + 1 rabbits with same colour -> x + 1 rabbits who all answer x
        # we have n rabbits who answer x
        # that means we need n / (x + 1) groups of x + 1 rabbits  

        for answer in answers:
            if rabbits[answer] % (answer + 1) == 0:
                result += answer + 1
            rabbits[answer] += 1
        
        return result

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people) 
        lightest = 0 
        heaviest = len(people) - 1 

        boats = 0

        while lightest <= heaviest: 
            if people[lightest] + people[heaviest] <= limit: 
                lightest += 1
            heaviest -= 1
            boats += 1 
        
        return boats
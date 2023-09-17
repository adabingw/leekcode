class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        
        potions = sorted(potions) 
        pairs = [0] * len(spells) 

        def binarysearch(spell): 
            left = 0
            right = len(potions)

            while (left < right):
                mid = left + (right - left) / 2
                if potions[mid] * spell < success:
                    left = mid + 1
                else:
                    right = mid
            return left


        for index, spell in enumerate(spells): 
            mid = binarysearch(spell)  
            pairs[index] = len(potions) - mid
        
        return pairs
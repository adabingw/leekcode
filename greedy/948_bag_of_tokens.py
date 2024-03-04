class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
        result = 0
        tokens.sort()

        while tokens:
            token = tokens.pop(0)
            if power >= token:
                power -= token
                result += 1
            
            elif len(tokens) == 0:
                break

            elif power <= token and result > 0:
                tokens.insert(0, token)
                token = tokens.pop()
                result -= 1
                power += token
        
        return result
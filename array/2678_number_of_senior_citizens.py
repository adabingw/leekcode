class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        elders = 0
        for detail in details:
            age = detail[11:13]
            if int(age) > 60:
                elders += 1
        
        return elders
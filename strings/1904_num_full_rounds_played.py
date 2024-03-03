class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        
        login = loginTime.split(":")
        logout = logoutTime.split(":")

        login = [int(t) for t in login]
        logout = [int(t) for t in logout]

        hours = 0
        minutes = 0

        rem = login[1] if login[1] % 15 == 0 else login[1] + 15 - login[1] % 15
        minutes += (60 - rem)
        rem2 = logout[1] if logout[1] % 15 == 0 else logout[1] - logout[1] % 15
        minutes += rem2

        if logout[0] < login[0]:
            hours = 24 - (login[0] + 1) % 25 + logout[0]
        elif logout[0] == login[0]:
            if logout[1] < login[1]:
                hours = 23
            else: 
                hours = 0
                minutes = max(rem2 - rem, 0)
        else:
            hours = logout[0] - (login[0] + 1)

        return hours * 4 + minutes / 15
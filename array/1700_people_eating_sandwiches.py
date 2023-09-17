from collections import Counter 

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students = Counter(students)
        for sandwich in sandwiches:
            if not students[sandwich]:
                break
            students[sandwich] -= 1
        return sum(students.values())
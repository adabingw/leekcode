class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(box)
        n = len(box[0])
        for row in box:
            where_to = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    where_to = j - 1
                elif row[j] == '#':
                    row[where_to], row[j] = row[j], row[where_to]
                    where_to -= 1
        
        rotate = []
        for i in range(n):
            rotate.append([])
            for j in range(m - 1, -1, -1):
                rotate[i].append(box[j][i])        
        
        return rotate
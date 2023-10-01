class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        
        result = 0

        positions = defaultdict(int)
        for i, r in enumerate(row):
            positions[r] = i
        
        for x_position in range(0, len(row) - 1, 2):
            x = row[x_position]

            # find partner number of x
            if x % 2 == 0:
                y = x + 1
            else: 
                y = x - 1

            y_position = positions[y]

            if abs(y_position - x_position) > 1:
                temp = row[x_position + 1]
                row[x_position + 1] = row[y_position]
                row[y_position] = temp
                positions[y] = x_position + 1
                positions[temp] = y_position
                result += 1
        
        return result

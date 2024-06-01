class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        n = (n - 1) % 14 + 1
        for i in range(n):
            new_cells = copy.deepcopy(cells)
            for index, cell in enumerate(cells):
                if index == 0 or index == 7:
                    new_cells[index] = 0
                elif cells[index - 1] != cells[index + 1]:
                    new_cells[index] = 0
                else:
                    new_cells[index] = 1
            cells = new_cells
        
        return cells
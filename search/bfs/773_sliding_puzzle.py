class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        moves = {
            0: {1, 3},
            1: {0, 2, 4},
            2: {1, 5},
            3: {0, 4},
            4: {1, 3, 5},
            5: {2, 4}
        }

        # visited board states
        visited = set()
        count = 0

        board_str = ""
        for row in board:
            for c in row:
                board_str += str(c)
        
        # (state of board, where the empty is)
        q = [(board_str, board_str.index('0'))]

        while q:
            new_q = []

            for s, i in q:
                visited.add(s)
                if (s) == "123450":
                    return count
                a = list(s)
                for m in moves[i]:
                    new_a = a[:]                    # deep copy
                    temp = new_a[i]
                    new_a[i] = new_a[m]
                    new_a[m] = temp
                    new_s = "".join(new_a)
                    if new_s not in visited:
                        new_q.append((new_s, m))
            
            count += 1
            q = new_q
        
        return -1

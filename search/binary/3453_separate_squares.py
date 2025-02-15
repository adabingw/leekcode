class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x : x[1])
        total_area = 0
        for _, _, l in squares:
            total_area += l * l
        target_area = total_area / 2
        highest_y = max(squares[i][1] + squares[i][2] for i in range(len(squares)))
        lowest_y = squares[0][1]
        epsilon = 10 ** -5
        left, right = lowest_y, highest_y
        while right - left > epsilon:
            mid = (left + right) / 2
            curr = 0
            for j in range(len(squares)):
                x0, y0, l0 = squares[j]
                if mid >= y0 + l0:
                    curr += l0 * l0
                elif y0 <= mid <= y0 + l0:
                    curr += (mid - y0) * l0
            if curr >= target_area:
                right = mid
            else:
                left = mid
        return left
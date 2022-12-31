/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePathsIII = function(grid) {
    let start = [-1, -1] 
    let directions = [
        [0, 1], 
        [0, -1], 
        [1, 0], 
        [-1, 0]
    ]
    let zeroes = 0

    for (var i = 0; i < grid.length; i++) {
        for (var j = 0; j < grid[i].length; j++) {
            if (grid[i][j] == 1) {
                start[0] = i 
                start[1] = j
            } else if (grid[i][j] == 0) zeroes++
        }
    }

    let paths = 0

    function getUniquePath(x, y, zero) {
        if (grid[x][y] == 2) {
           if (zero - 1 == zeroes) paths++;
            return;
        }

        if (grid[x][y] === -1 || grid[x][y] == -2) return;

        grid[x][y] = -2;

        for (var m = 0; m < directions.length; m++) {
            const i = x + directions[m][0];
            const j = y + directions[m][1];
            if (i >= 0 && i < grid.length && j >= 0 && j < grid[0].length)
                getUniquePath(i, j, zero + 1);
        }
        grid[x][y] = 0;
    }

    getUniquePath(start[0], start[1], 0)
    return paths
};
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function(n, edges, hasApple) {
    let a = []
    for (let i = 0; i < n; i++) a.push([])
    for (let x of edges) {
        a[x[0]].push(x[1]);
        a[x[1]].push(x[0]);
    }

    // we can access nodes a[i] at node i
    // we start at node 0 
    return dfs(-1, 0, a, hasApple);
};

function dfs(prev, curr, a, hasApple) {
    let ans = 0;
    for (let x of a[curr]) {
        // explore node x if we haven't visited it before
        if (x !== prev) {
            let res = dfs(curr, x, a, hasApple);
            if (res > 0 || hasApple[x]) {
                // cost + 2, to and back 
                ans += (res + 2);
            }
        }
    }
    return ans;
}
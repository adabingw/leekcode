/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @return {number[]}
 */

var countSubTrees = function(n, edges, labels) {
    let a = []
    let ans = []
    for (let i = 0; i < n; i++) a.push([])
    for (let x of edges) {
        a[x[0]].push(x[1]);
        a[x[1]].push(x[0])
    }
    
    for (let i = 0; i < a.length; i++) ans.push(1)

    dfs(-1, 0, a, labels, ans)
    return ans
};

function dfs(prev, curr, a, labels, array) {
    let ans = new Array(26).fill(0);

    for (let x of a[curr]) {
        if (prev != x) {
            const res = dfs(curr, x, a, labels, array);  
            for (let i = 0; i < 26; i++)  ans[i] += res[i];
        }
    }

    array[curr] = ++ans[labels.charCodeAt(curr) - 'a'.charCodeAt(0)];
    return ans;
}
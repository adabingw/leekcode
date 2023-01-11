/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b) => a[0] - b[0])
    let result = [intervals[0]]
    for (var i = 0; i < intervals.length; i++) {
        let res = result[result.length - 1] 
        if (intervals[i][0] <= res[1]) result[result.length - 1][1] = Math.max(intervals[i][1], res[1])
        else result.push(intervals[i])
    }
    return result;
};
/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    let i = 0;
    let arrows = 0;
    points.sort((a,b) => a[0] - b[0])
    
    while(i < points.length){
        let start = points[i][0]
        let end = points[i][1]
        i++
        while (i < points.length && points[i][0] <= end && points[i][1] >= start){
            start = Math.max(start, points[i][0]);
            end = Math.min(end, points[i][1]);
            i++
        }
        arrows++;
    }
    return arrows;
};
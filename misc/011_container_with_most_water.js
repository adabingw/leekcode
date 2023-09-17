/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max_area = 0;

    while(left < right) {
        max_area = Math.max(max_area, Math.min(height[right], height [left]) * (right - left) );
        if(height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max_area;
};
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let closest_sum = Number.MAX_VALUE

	nums = nums.sort((a, b) => a - b)

    for(let i = 0; i < nums.length - 2; i++){
        let low = i + 1
        let high = nums.length - 1
        let sum = 0

        while(low < high){
            sum = nums[i] + nums[low] + nums[high]
            if (Math.abs(target - sum) < Math.abs(closest_sum)) closest_sum = target - sum
            if (sum < target) low++
            else high--
        }
    }
    return target - closest_sum
};
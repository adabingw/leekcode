/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    const results = []
	if (nums.length < 4) return results

	nums = nums.sort((a, b) => a - b)

    for (let i = 0; i < nums.length - 3; i++) {
        for (let j = i + 1; j < nums.length - 2; j++) {
            let low = j + 1
            let high = nums.length - 1
            let sum = 0
            
            while (low < high) {
                sum = nums[i] + nums[low] + nums[high] + nums[j]
                if (sum === target) {
                    results.push([nums[i], nums[j], nums[low], nums[high]])

                    // to avoid duplicates
                    while (nums[low + 1] === nums[low]) low++
                    while (nums[high - 1] === nums[high]) high--
                    
                    low++
                    high--
                } else if (sum < target) low++
                else high--
            }
            while(nums[j+1] === nums[j]) j++
        }

        while(nums[i+1] === nums[i]) i++
    }
    return results
};
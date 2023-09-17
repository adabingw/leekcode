/**
 * @param {number[]} nums
 * @return {number[][]}
 */
function threeSum(nums) {

	const results = []
	if (nums.length < 3) return results

	nums = nums.sort((a, b) => a - b)

    for (let i = 0; i < nums.length; i++) {
        let low = i + 1
        let high = nums.length - 1
        let sum = 0
        
        while (low < high) {
            sum = nums[i] + nums[low] + nums[high]
            
            if (sum === 0) {
                results.push([nums[i], nums[low], nums[high]])

                // to avoid duplicates
                while (nums[low + 1] === nums[low]) low++
                while (nums[high - 1] === nums[high]) high--
                
                low++
                high--
            } else if (sum < 0) low++
            else high--
        }
        while(nums[i+1] === nums[i]) i++
    }
    return results
};
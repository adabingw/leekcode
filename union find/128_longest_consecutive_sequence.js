/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let sequence = 0 
    const set = new Set(nums);
    for (let i of set) {
        let increment = 1
        let currSequence = 1
        if (!set.has(i - 1)) {
            while (set.has(i + increment)) {
                increment++
                currSequence++
            }
            if (currSequence > sequence) sequence = currSequence
        }
    }
    return sequence
};
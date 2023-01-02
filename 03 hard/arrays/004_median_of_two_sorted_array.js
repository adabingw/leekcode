/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let number = nums1.concat(nums2)
    console.log(number)
    
    number.sort(function(a, b) {
      if( a === Infinity ) 
        return 1; 
      else if( isNaN(a)) 
        return -1;
      else 
        return a - b;
    });
    
    console.log(number)
    
    if (number.length == 0) {
        return;
    } else if (number.length == 1) {
        return number[0]
    } else if (number.length % 2 == 0) {
        console.log(number.length / 2)
        let n1 = number[number.length/2 - 1]
        let n2 = number[number.length/2]
        return (n1 + n2) / 2
    } else {
        let n = number[Math.floor(number.length / 2)]
        return n
    }

};
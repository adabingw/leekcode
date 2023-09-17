/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let max = 0;
    let start = 0; 
    for (var i = 0; i < s.length; i++) {
        for (var j = start; j < i; j++) {
            if (s[i] == s[j]) {
                start = j + 1;
                break;
            }
        }

        if (i - start + 1 > max) max = i - start + 1;
    }

    return max;
};
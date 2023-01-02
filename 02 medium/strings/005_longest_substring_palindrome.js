var longestPalindrome = function(s) {
    
	if (s.length <= 1) return s;
    if (s.length == 2) {
        if (s[0] == s[1]) return s; 
        else return s[0];
    }
	
	let palindrome = '';
    for (var i = 0; i < s.length; i++) {
        for (var j of [0, 1]) {
            let left = i;
            let right = i + j;
            while (left >= 0 && s[left] == s[right]) {
                left--;
                right++;
            }
            
            if ((right - left - 1) > palindrome.length) {
                palindrome = s.substring(left + 1, right);
            }
            
        }
    }
    return palindrome;
}
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let str = String(x)
    if (str.length == 1) {
        return x
    }
    
    // funny
    var reverseX = parseInt(String(x).split('').reverse((a,b) => a - b).join(''));
    if(reverseX > Math.pow(2,31) - 1){
      return 0;
    }

    let s = String(x).split("").reverse().join("")
    let neg = false
    let last0 = false
    if (s[0] == '0') s = s.substring(1)

    if (s[s.length - 1] == '-') {
        s = s.substring(0, s.length - 1)
        s = '-' + s
    }        
    
    return parseInt(s)
};
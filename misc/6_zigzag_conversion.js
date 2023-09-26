/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (s.length <= numRows || numRows == 1) return s
        
    let result = []
    for (var i = 0; i < numRows; i++) result.push([])
    
    let tracker = 0
    let zig = numRows - 2
    
    for (var i = 0; i < s.length; i++) {
        if (tracker != numRows) {
            result[tracker].push(s[i])
            tracker++
        } else {
            if (numRows == 2) {
                tracker = 0
                result[tracker].push(s[i])
                tracker++
            } else {
                for (var j = 0; j < numRows; j++) {
                    if (j == zig) result[j].push(s[i])
                    else result[j].push(' ')
                }
                if (zig == 1) {
                    tracker = 0
                    zig = numRows - 2
                } else { zig-- }   
            }
        }
    }
    
    let zigzag = ""
    for (var i = 0; i < numRows; i++) {
        for (var j of result[i]) {
            if (j != ' ') zigzag += j
        }
    }
    return zigzag
};
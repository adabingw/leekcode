/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    let pattern_map = {}
    let s_arr = s.split(" ");

    if (s_arr.length !== pattern.length) return false;
    if (new Set (pattern.split("")).size !== new Set(s_arr).size) return false;

    for (var i = 0; i < pattern.length; i++) {
        if ((pattern_map[pattern[i]])) {
            if (pattern_map[pattern[i]] !== s_arr[i]) return false;
        } else pattern_map[pattern[i]] = s_arr[i];          
    }
    return true;
};
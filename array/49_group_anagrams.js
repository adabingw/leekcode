/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let result = []
    let res_map = {}
    for (var i = 0; i < strs.length; i++) {
        let word = strs[i].split('').sort().join('');
        if (res_map[word]) res_map[word].push(strs[i])
        else res_map[word] = [strs[i]]
    }
    for (var m in res_map) {
        result.push(res_map[m])
    }

    return result
};
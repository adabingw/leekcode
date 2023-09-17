/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let to_delete = 0; 

    for (var i = 0; i < strs[0].length; i++) {
        let last_index = 0;
        for (var j = 0; j < strs.length; j++) {
            if (last_index > alphabet.indexOf(strs[j][i])) {
                to_delete++;
                break;
            } else {
                last_index = alphabet.indexOf(strs[j][i])
            }
        }
    }

    return to_delete;
};
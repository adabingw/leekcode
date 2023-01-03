/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    for (var i = 0; i < word.length - 1; i++) {
        if (word.charCodeAt(i) - 65 <= 25 && word.charCodeAt(i + 1) - 65 > 25 && i != 0) return false;
        if (word.charCodeAt(i) - 65 > 25 && word.charCodeAt(i + 1) - 65 <= 25) return false;
    }
    return true;
};
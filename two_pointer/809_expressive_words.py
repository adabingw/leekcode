class Solution {
public:
    int expressiveWords(string s, vector<string>& words) {
        int res = 0;

        for (auto word : words) {
            if (stretch(word, s)) res++;
        }

        return res;
    }

    bool stretch(const string& word, const string& target) {
        int i = 0, j = 0;

        while (i < word.size() && j < target.size()) {
            if (word[i] != target[j]) return false;

            int len1 = 1, len2 = 1;

            while (i + 1 < word.size() && word[i] == word[i + 1]) {
                i++;
                len1++;
            }

            while (j + 1 < target.size() && target[j] == target[j + 1]) {
                j++;
                len2++;
            }

            if (len1 > len2 || (len1 < len2 && len2 < 3)) return false;

            i++;
            j++;
        }

        return i == word.size() && j == target.size();
    }
};
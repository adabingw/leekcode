class Solution {
public:
    long long minimumSteps(string s) {
        int zero = 0;
        long long res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                res += i - zero;
                zero += 1;
            }
        }

        return res;
    }
};
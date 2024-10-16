class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        int n = skill.size();
        int s = skill.at(0) + skill.at(n - 1);
        long long res = skill.at(0) * skill.at(n - 1);
        for (int i = 1; i < n / 2; i++) {
            if (skill.at(i) + skill.at(n - i - 1) != s) {
                return -1;
            } else {
                res += skill.at(i) * skill.at(n - i - 1);
            }
        }

        return res;
    }
};
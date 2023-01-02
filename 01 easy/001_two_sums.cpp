#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        bool breaks = false;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (nums.at(i) + nums.at(j) == target && i != j) {
                    result.push_back(i);
                    result.push_back(j);
                    breaks = true;
                    break;
                }
            } if (breaks == true) {
                    break;
                }
        }
        return result;
    }
};
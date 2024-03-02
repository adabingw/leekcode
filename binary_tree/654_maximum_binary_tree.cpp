/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getMax(vector<int>& nums, int left, int right) {
        int max = left; 
        for (int i = left; i < right; i++) {
            if (nums.at(max) < nums.at(i)) max = i;
        }
        return max; 
    }
    
    TreeNode* construct(vector<int>& nums, int left, int right) {
        if (left == right) return nullptr; 

        int max = getMax(nums, left, right);
        cout << max << " " << nums.at(max) << endl;

        TreeNode* node = new TreeNode(nums.at(max)); 
        node->left = construct(nums, left, max); 
        node->right = construct(nums, max + 1, right); 
        return node; 
    }

    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        TreeNode* root = construct(nums, 0, nums.size()); 
        return root; 
    }
};
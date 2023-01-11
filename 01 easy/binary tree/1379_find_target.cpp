/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    public:
        TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
            if (original == nullptr || cloned == nullptr) return nullptr;
            if (cloned->val == target->val) return cloned;
    
            TreeNode* l = getTargetCopy(original->left, cloned->left, target); 
            TreeNode* r = getTargetCopy(original->right, cloned->right, target); 
    
            if (l == nullptr) return r; 
            else return l;
        }
};
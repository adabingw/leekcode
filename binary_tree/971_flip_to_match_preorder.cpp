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

#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> nodes;
    int i = 0;
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        if (flip(root, voyage)) return nodes;
        else return vector<int>{-1};
    }

    bool flip(TreeNode* root, vector<int>& voyage) {
        if (root == nullptr) return true; 
        if (root->val != voyage[i++]) return false; 
        if (root->left != nullptr && root->left->val != voyage[i]) {
            nodes.push_back(root->val); 
            return flip(root->right, voyage) && flip(root->left, voyage);
        }
        return flip(root->left, voyage) && flip(root->right, voyage);
    }
};
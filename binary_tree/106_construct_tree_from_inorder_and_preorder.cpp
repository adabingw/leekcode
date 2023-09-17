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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size() - 1;
        return build(inorder, postorder, 0, n, n);
    }

    TreeNode* build(vector<int>& inorder, vector<int>& postorder, int start, int endi, int& post) {
        if(start > endi) return nullptr;

        // root node will always be at the end of the postorder 
        TreeNode* root = new TreeNode(postorder[post--]);

        // find root index in inorder traversal 
        int index = find(begin(inorder), end(inorder), root->val) - begin(inorder);

        // left tree is to the left of the node, right tree is to the right
        root->right = build(inorder, postorder, index + 1, endi, post);
        root->left  = build(inorder, postorder, start, index - 1, post);
        
        return root;
    }
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    TreeNode* maketree(vector<int>& vec, int start, int end) {
        if(start == end) return nullptr;
        
        int mid = start + (end - start) / 2;
        TreeNode* root = new TreeNode(vec[mid]);
        
        root->left = maketree(vec, start, mid);
        root->right =  maketree(vec, mid + 1, end);
        
        return root;
    }
    
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> vec;
        if(!head) return nullptr;
        for(auto temp = head; temp!=NULL; temp = temp->next) {
            vec.push_back(temp->val);
        }
        TreeNode* root = maketree(vec, 0, vec.size());
        return root;
    }
};
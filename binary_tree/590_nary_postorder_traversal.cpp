/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public: 
    vector<int> postorder(Node* root) {
        vector<int> traversal; 
        if (!root) return traversal;
        if (root->children.size() == 0) {
            traversal.push_back(root->val); 
            return traversal;
        }

        for (int i = 0; i < root->children.size(); i++) {
            vector<int> childTraversal = postorder(root->children.at(i)); 
            traversal.insert(traversal.end(), childTraversal.begin(), childTraversal.end());
        }
        traversal.push_back(root->val); 
        return traversal;
    }
};
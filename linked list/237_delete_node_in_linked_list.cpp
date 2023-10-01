struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    void deleteNode(ListNode* node) {
        if (node->next != nullptr) {
            node->val = node->next->val; 
            node->next = node->next->next;
        } else node = nullptr;
    }
};
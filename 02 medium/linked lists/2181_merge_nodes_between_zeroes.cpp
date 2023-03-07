struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* root = new ListNode(0); 
        ListNode* temp = head->next; 
        ListNode* temp_root = root;
        while (temp) {
            int val = 0;
            while (temp->val != 0) {
                val += temp->val; 
                temp = temp->next;
            }
            ListNode* node = new ListNode(val); 
            temp_root->next = node; 
            temp_root = temp_root->next; 
            temp = temp->next;
        }  
        return root->next;
    }
};
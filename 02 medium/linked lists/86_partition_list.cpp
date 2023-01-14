struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* small = new ListNode(0); 
        ListNode* big = new ListNode(0);

        ListNode* small_temp = small; 
        ListNode* big_temp = big; 

        while (head != nullptr) {
            if (head->val < x) {
                small->next = head; 
                small = small->next; 
                head = head->next;
                small->next = nullptr; 
            } else {
                big->next = head; 
                big = big->next; 
                head = head->next;
                big->next = nullptr; 
            }
        }

        small->next = big_temp->next;
        return small_temp->next;
    }
};
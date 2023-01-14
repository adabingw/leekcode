struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr) return nullptr;
        
        ListNode* temp = head; 
        int t = 0;

        while (temp->next != nullptr) {
            temp = temp->next; 
            t++;
        }
        
        ListNode* curr = head;
                
        if (t + 1 == n) {
            head = head->next;
            return head;
        }
        
        for (int i = 0; i < t - n; i++) curr = curr->next; 
        
        curr->next = curr->next->next;
        return head;
    }
};
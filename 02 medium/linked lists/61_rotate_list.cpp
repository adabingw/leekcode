struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode* temp = head; 
        int count = 1;
        
        if (head == nullptr || head->next == nullptr || k == 0) return head;
        
        while (temp->next != nullptr) {
            count++;
            temp = temp->next;   
        }

        if (count == k) return head;
        
        temp->next = head;
        
        k = count - (k % count) - 1;        
        temp = head;
        
        while (k--) temp = temp->next;
        
        ListNode* temp2 = temp->next;
        temp->next = nullptr;
        head = temp2;
        return head;
    }
};
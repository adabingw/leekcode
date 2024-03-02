struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr) return nullptr;
        ListNode* fast = head; 
        ListNode* slow = head; 
        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next; 
            slow = slow->next;

            if (fast == slow) break;
        }

        if (fast == nullptr || fast->next == nullptr) return nullptr;
        while (head != slow) {
            head = head->next;
            slow = slow->next;
        }
        return head;
    }
};
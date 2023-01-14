struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Floyd’s Cycle-Finding Algorithm // fast slow approach // 2 pointers // "tortoise and the hare algorithm"

// Approach: This is the fastest method and has been described below:

// Traverse linked list using two pointers.

// Move one pointer(slow_p) by one and another pointer(fast_p) by two.

// If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) return false;
        ListNode* fast = head; 
        ListNode* slow = head; 
        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next; 
            slow = slow->next;

            if (fast == slow) return true;
        }
        return false;
    }
};
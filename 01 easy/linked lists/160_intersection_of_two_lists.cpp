struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* a = headA; 
        ListNode* b = headB; 

        if (a == nullptr || b == nullptr) return nullptr; 

        while (a != nullptr && b != nullptr && a != b) {

            a = a->next; 
            b = b->next; 

            if (a == b) return a;

            if (a == nullptr) a = headA; 
            if (b == nullptr) b = headB;
        }

        return a;
    }
};
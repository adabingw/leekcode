struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int curr = 0;
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == nullptr) {
            curr++; 
            return nullptr;
        }

        head->next = removeNthFromEnd(head->next, n); 
        curr++; 
        return curr - 1 == n ? head->next : head;
    }
};
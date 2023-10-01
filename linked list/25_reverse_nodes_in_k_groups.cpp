struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int count(ListNode* head){
        ListNode* p = head;
        int c = 0;
        while (p != nullptr){
            c++;
            p = p->next;
        }
        return c;
    }

    ListNode* reverse(ListNode* head, int k, int rem){
        if (rem < k) return head;
        ListNode* cur = head, *next = nullptr, *prev = nullptr; 
        int c = 0;
        while (cur != nullptr && c < k){
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;     
            c++;
        }
        if (next != nullptr) head->next = reverse(next, k, rem - k);
        return prev;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        return reverse(head, k, count(head));
    }
};
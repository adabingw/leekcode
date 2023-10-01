
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head; 

        ListNode* temp = nullptr;
        ListNode* fast = head; 
        ListNode* slow = head; 

        while (fast && fast->next) {
            temp = slow; 
            slow = slow->next; 
            fast = fast->next->next; 
        }

        temp->next = nullptr; 

        ListNode* left = sortList(head); 
        ListNode* right = sortList(slow); 

        ListNode* mergedList = mergeList(left, right); 
        return mergedList; 
    }

    ListNode* mergeList(ListNode* l1, ListNode* l2) {
        ListNode* root = new ListNode(0); 
        ListNode* curr = root; 

        while (l1 && l2) {
            if (l1->val <= l2->val) {
                curr->next = l1; 
                l1 = l1->next;
            } else {
                curr->next = l2; 
                l2 = l2->next;
            }
            curr = curr->next;
        }

        if (l1) {
            curr->next = l1; 
            l1 = l1->next;
        } else if (l2) {
            curr->next = l2; 
            l2 = l2->next;
        }

        return root->next;
    }
};
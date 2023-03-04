/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // ListNode* removeElements(ListNode* head, int val) {
    //     if (head == nullptr) return nullptr;
    //     ListNode* prev = nullptr; 
    //     ListNode* curr = head; 
    //     while (curr != nullptr) {
    //         cout << curr->val << endl;
    //         if (curr->val == val && prev != nullptr) {
    //             cout << curr->val << " and in here " << endl;
    //             prev->next = curr->next; 
    //             curr = curr->next;
    //         } else if (curr->val == val && prev == nullptr) {
    //             head = head->next;
    //             curr = head; 
    //             continue;
    //         } else {
    //             prev = curr; 
    //             curr = curr->next;
    //         }
    //     }
    //     return head;
    // }

    ListNode* removeElements(ListNode* head, int val) {
        if (head == nullptr) return nullptr; 
        head->next = removeElements(head->next, val); 
        return head->val == val ? head->next : head;
    }
};
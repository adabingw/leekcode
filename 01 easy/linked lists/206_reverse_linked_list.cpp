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

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void printList(ListNode* head) {
        ListNode* temp = head;
        while (temp != nullptr) {
            cout << temp->val;
            temp = temp->next;
        } cout << endl;
    }
    
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = nullptr; 
        while (head != nullptr) {
            ListNode* next = head->next; 
            head->next = curr; 
            curr = head; 
            head = next; 
            printList(curr);
        }
        return curr;
    }
};
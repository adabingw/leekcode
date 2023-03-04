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
    void printList(ListNode* head) {
        ListNode* temp = head;
        while(temp) {
            cout << temp->val << " "; 
            temp = temp->next;
        } cout << endl << endl;;
    }
    ListNode* insertionSortList(ListNode* head) {
        ListNode* root = new ListNode(0); 
        ListNode* prev = root; 
        while (head != nullptr) {
            ListNode* temp = head->next; 

            // start at root if value we're looking at is less than the current node we're pointing at
            if (prev->val >= head->val) prev = root; 

            // find correct place to put stuff
            while (prev->next != nullptr && prev->next->val < head->val) {
                prev = prev->next; 
            }

            // insert between prev and prev->next 
            head->next = prev->next; 
            prev->next = head; 

            // resume sorting
            head = temp;
        }
        return root->next;
    }
};
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
    int count(ListNode* head) {
        int size = 0; 
        ListNode* temp = head; 
        while (temp) {
            size++; 
            temp = temp->next;
        }
        return size;
    }

    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        vector<ListNode*> list; 
        int size = count(head); 
        int q = size / k; 
        int m = size % k;
        ListNode* temp = head;
        for (int i = 0; i < k; i++) {
            if (q == 0 && m == 0) list.push_back(nullptr); 
            else if (q == 0 && m != 0) {
                list.push_back(temp); 
                ListNode* next = temp->next; 
                temp->next = nullptr;
                temp = next; 
                m--; 
            } else  {
                int amount = 0; 
                if (m == 0) amount = q - 1; 
                else {
                    amount = q; 
                    m--;
                }
                list.push_back(temp); 
                ListNode* next = temp->next;
                while (amount > 0 && next) {
                    temp = temp->next; 
                    next = next->next;
                    amount--;
                }
                temp->next = nullptr; 
                temp = next;
            }
        }
        return list; 
    }
};
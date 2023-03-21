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

// RESERVOIR SAMPLING
// The reservoir sampling algorithm is intended to sample k elements from an population of unknown size. 
// In our case, the k happens to be one.

class Solution {
public:
    ListNode* head = nullptr;

    Solution(ListNode* head) {
        this->head = head;
    }
    
    int getRandom() {
        int scope = 1;
        int chosen_value = 0;
        ListNode* curr = head; 

        while (curr) {
            float random = rand() % 1; 
            if (rand() % scope == 0) {
                chosen_value = curr->val;
            }
            curr = curr->next; 
            scope += 1;
        }

        return chosen_value;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
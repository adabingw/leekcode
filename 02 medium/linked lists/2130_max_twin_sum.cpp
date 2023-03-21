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
    int pairSum(ListNode* head) {
        ListNode* fast = head; 
        ListNode* slow = head; 
        vector<int> left, right; 

        while (fast && fast->next) {
            left.push_back(slow->val); 
            slow = slow->next; 
            fast = fast->next->next; 
        }

        while (slow) {
            right.push_back(slow->val); 
            slow = slow->next; 
        }

        int i = 0; 
        int max = 0; 
        for (int i = 0; i < left.size(); i++) {
            int l = left.at(left.size() - 1 - i); 
            int r = right.at(i); 
            max = (l + r) > max ? (l + r) : max; 
        }

        return max;
    }
};
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode* even = new ListNode(0); 
        ListNode* odd = new ListNode(0); 
        int index = 0; 
        ListNode* temp = head; 
        ListNode* tempEven = even; 
        ListNode* tempOdd = odd;
        while (temp != nullptr) {
            if (index % 2 == 0) {
                tempEven->next = new ListNode(temp->val); 
                tempEven = tempEven->next; 
            } else {
                tempOdd->next = new ListNode(temp->val); 
                tempOdd = tempOdd->next; 
            }
            temp = temp->next; 
            index++;
        }
        tempEven->next = odd->next;
        return even->next;
    }
};
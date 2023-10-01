struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int count(ListNode* head) {
        ListNode* temp = head;
        int c = 0;
        while (temp){
            c++;
            temp = temp->next;
        }
        return c;
    }

    ListNode* reverse(ListNode* head, int k){
        ListNode* prev = nullptr;
        ListNode* last = head;
        int c = 0;
        while (head != nullptr && c < k){
            ListNode* temp = head->next;
            head -> next = prev;
            prev = head;
            head = temp;     
            c++;
        }
        last->next = head;
        return prev;
    }

    ListNode* reverseEvenLengthGroups(ListNode* head) {
        int curr = 1; 
        ListNode* prev = nullptr;
        ListNode* temp = head; 
        while (temp) {
            if (curr % 2 == 0 && count(temp) >= curr) {
                prev->next = reverse(temp, curr);
                if (temp) {
                    prev = temp;
                    temp = temp->next;
                } 
            } else if (count(temp) < curr && count(temp) % 2 == 0) {
                prev->next = reverse(temp, count(temp));
                if (temp) {
                    prev = temp;
                    temp = temp->next;
                }
            } else if (curr % 2 != 0) {
                int w = 0; 
                while (w < curr && temp) {
                    temp = temp->next; 
                    if (prev == nullptr) prev = head;
                    else prev = prev->next; 
                    w++;
                }
            }
            curr++; 
        }

        return head;
    }
};
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
		
        // place dummy node before head
        // dummyNode->1->2->3->4
        ListNode* dummyNode = new ListNode();
        
        // currNode = 1
        ListNode* prevNode = dummyNode;
        ListNode* currNode = head;
        
        while (currNode != nullptr && currNode->next != nullptr) {
            // change the next pointer of prevNode to point to currNode->next
            // dummyNode->2->3->4 
            prevNode->next = currNode->next;
            // change currNode->next to the next of next of prevNode
            // 1->3
            currNode->next = prevNode->next->next;
            // dummyNode->2->1->3->4
            prevNode->next->next = currNode;
            
            prevNode = currNode;
            currNode = currNode->next;
        }
        
        return dummyNode->next;
    }
};
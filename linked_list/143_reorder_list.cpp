#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        vector<ListNode*> nodes; 
        ListNode* temp = head;
        while (temp != nullptr) {
            nodes.push_back(temp);
            temp = temp->next;
        } 

        int left = 1, right = nodes.size() - 1; 

        for (int i = 0; i < nodes.size(); i++) {
            if (i % 2) head->next = nodes.at(left++);
            else head->next = nodes.at(right--);
            head = head->next;
        }
        head->next = nullptr;
    }
};
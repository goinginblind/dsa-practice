// Remove the nth node from the end of a singly-linked list.

#include <iostream>
#include <unordered_map>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* removeNthFromEnd(ListNode* head, int n) {
    unordered_map<int, ListNode*> node_map;
    int curr_node_index = 0;
    ListNode* ptr = head;
    while (ptr) {
        curr_node_index++;
        node_map[curr_node_index] = ptr;
        ptr = ptr->next;
    }
    if (curr_node_index - n > 0) {
        ListNode* node_rewire = node_map[curr_node_index - n];
        node_rewire->next = node_rewire->next->next;
    } else if (curr_node_index - n == 0) {
        head = head->next;
    }
    return head;
}


void printList(ListNode* head) {
    while (head) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    int n = 2;
    head = removeNthFromEnd(head, n);
    printList(head);

    return 0;
}
Reverse Linked List (Leetcode #206)
===============================
### Easy

Reverse a singly linked list.

### Example:
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
### Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

Solution
========
```c++
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
// Space: O(1)
class Solution {
public:
    ListNode* reverseList(ListNode* head) {    
        if (head == NULL || head->next == NULL)
            return head;
        ListNode* ptr0 = NULL;
        ListNode* ptr1 = head;
        ListNode* ptr2 = NULL;
        while (ptr1 != NULL) {
            // reverse the link.
            ptr2 = ptr1->next;
            ptr1->next = ptr0;
            // Go to the next iteration.
            ptr0 = ptr1;
            ptr1 = ptr2;
        }
        head = ptr0;
        return ptr0;
    }
    // Space: O(n)
    // ListNode* reverseList(ListNode* head) {    
    //     if (head == NULL)
    //         return NULL;
    //     std::vector<int> tmp;
    //     auto ptr = head;
    //     while (ptr) {
    //         tmp.insert(tmp.begin(), ptr->val);
    //         ptr = ptr->next;
    //     }            
    //     ListNode* new_head = NULL;
    //     ListNode* tail = NULL;
    //     for (const auto& elem: tmp) {
    //         auto node = new ListNode(elem);
    //         if (new_head==NULL) {
    //             new_head = node;
    //             tail = node;
    //         } else {
    //             tail->next = node;
    //             tail = node;
    //         }
    //     }
    //     return new_head;
    // }
};

```

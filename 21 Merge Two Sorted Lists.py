"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

List 1:
(1)->(2)->(4)->

List 2:
(1)->(3)->(4)->

Merged List:
(1)->(1)->(2)->(3)->(4)->(4)->

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)  # dummy head to avoid edge cases
        curr_merged = dummy  # pointer to build the new list

        curr1 = list1
        curr2 = list2

        while curr1 is not None or curr2 is not None:
            if curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:
                    curr_merged.next = ListNode(curr1.val)
                    curr1 = curr1.next
                else:
                    curr_merged.next = ListNode(curr2.val)
                    curr2 = curr2.next
                curr_merged = curr_merged.next

            elif curr1 is not None:  # only list1 has nodes left
                curr_merged.next = ListNode(curr1.val)
                curr1 = curr1.next
                curr_merged = curr_merged.next

            elif curr2 is not None:  # only list2 has nodes left
                curr_merged.next = ListNode(curr2.val)
                curr2 = curr2.next
                curr_merged = curr_merged.next

        return dummy.next  # skip the dummy head


def build_linked_list(values):
    head = current = ListNode()
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return head.next


def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print("->".join(result))


if __name__ == "__main__":
    s = Solution()

    # Example 1
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    merged = s.mergeTwoLists(list1, list2)
    print("Example 1 Output:")
    print_linked_list(merged)

    # Example 2
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    merged = s.mergeTwoLists(list1, list2)
    print("Example 2 Output:")
    print_linked_list(merged)

    # Example 3
    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    merged = s.mergeTwoLists(list1, list2)
    print("Example 3 Output:")
    print_linked_list(merged)

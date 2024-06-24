"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy_head = ListNode(-1000, head)
        prev_ptr = dummy_head
        cur_ptr = head
        while cur_ptr is not None:
            if cur_ptr.val == prev_ptr.val:
                prev_ptr.next = cur_ptr.next
            else:
                # If we remove a node, we don't want to move prev_ptr or else it will
                # point to the same node as cur_ptr. Basically, because a node was deleted
                # prev_ptr is still pointing to the previous node once cur_ptr is advanced
                prev_ptr = prev_ptr.next
            cur_ptr = cur_ptr.next

        return dummy_head.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(1, ListNode(2)))
    output = Solution().deleteDuplicates(head)
    assert listNodeToList(output) == [1, 2]

    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    output = Solution().deleteDuplicates(head)
    assert listNodeToList(output) == [1, 2, 3]

    output = Solution().deleteDuplicates(None)
    assert output is None

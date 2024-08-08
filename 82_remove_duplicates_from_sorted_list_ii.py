"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""
from collections import defaultdict
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

        counts = defaultdict(int)

        node = head
        while node:
            counts[node.val] += 1
            node = node.next

        dummy_head = ListNode(-1000, head)
        node = head
        prev = dummy_head
        while node:
            if counts[node.val] > 1:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy_head.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    output = Solution().deleteDuplicates(head)
    assert listNodeToList(output) == [1, 2, 5]

    head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    output = Solution().deleteDuplicates(head)
    assert listNodeToList(output) == [2, 3]

    output = Solution().deleteDuplicates(None)
    assert listNodeToList(output) == []

    head = ListNode(1)
    output = Solution().deleteDuplicates(head)
    assert listNodeToList(output) == [1]

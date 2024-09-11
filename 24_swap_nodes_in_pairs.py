"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""
from typing import Optional

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("*****")
        if not head:
            return None
        dummy_head = ListNode(-1, head)
        cur_node = head
        prev = dummy_head
        while cur_node is not None and cur_node.next is not None:
            next = cur_node.next
            print("swapping", cur_node.val, next.val)
            prev.next = next
            temp = next.next
            next.next = cur_node
            cur_node.next = temp

            prev = prev.next.next
            cur_node = temp

        print(listNodeToList(dummy_head.next))
        return dummy_head.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    output = Solution().swapPairs(head)
    assert listNodeToList(output) == [2, 1, 4, 3]

    output = Solution().swapPairs(None)
    assert output is None

    head = ListNode(1)
    output = Solution().swapPairs(head)
    assert listNodeToList(output) == [1]

    head = ListNode(1, ListNode(2, ListNode(3)))
    output = Solution().swapPairs(head)
    assert listNodeToList(output) == [2, 1, 3]

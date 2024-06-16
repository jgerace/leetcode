"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""
from typing import Optional

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseWithSinglePass(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        This solution finds the leftmost boundary and then puts every subsequent node behind it
        until the rightmost boundary
        Ex: left = 2, right = 5
        1    2    3    4    5    6
        pl  cur  nxt

        We will iterate from 3 until 5 and move each node to the pl.next position
        # 1
        1    2    3    4    5    6
        pl  cur  nxt
           ^------

        # 2
        1    3    2    4    5    6
        pl  cur       nxt
           ^-----------

        # 3
        1    4    3    2    5    6
        pl  cur            nxt
           ^----------------

        # end
        1    5    4    3    2    6
        pl  cur
        """

        if not head:
            return None
        print("input", listNodeToList(head))

        dummyHead = ListNode(-1000, head)

        prevLeft = dummyHead
        for _ in range(left-1):
            prevLeft = prevLeft.next

        current = prevLeft.next

        for _ in range(right - left):
            next = current.next
            current.next = next.next
            next.next = prevLeft.next
            prevLeft.next = next
            print(listNodeToList(dummyHead.next))

        return dummyHead.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        leftPtr = head
        for _ in range(left-1):
            leftPtr = leftPtr.next

        nodes = []
        for _ in range(right - left + 1):
            nodes.append(leftPtr)
            leftPtr = leftPtr.next

        start = 0
        end = right - left
        while start < end:
            temp = nodes[start].val
            nodes[start].val = nodes[end].val
            nodes[end].val = temp
            start += 1
            end -= 1
        return head


if __name__ == "__main__":
    input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output = Solution().reverseWithSinglePass(input, 3, 4)
    assert listNodeToList(output) == [1, 2, 4, 3, 5]

    input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    output = Solution().reverseWithSinglePass(input, 2, 5)
    assert listNodeToList(output) == [1, 5, 4, 3, 2, 6]

    input = ListNode(5)
    output = Solution().reverseBetween(input, 1, 1)
    assert listNodeToList(output) == [5]

    input = ListNode(5, ListNode(2))
    output = Solution().reverseBetween(input, 1, 2)
    assert listNodeToList(output) == [2, 5]

    output = Solution().reverseBetween(None, 1, 1)
    assert output is None

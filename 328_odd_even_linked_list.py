"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:

    The number of nodes in the linked list is in the range [0, 10^4].
    -10^6 <= Node.val <= 10^6
"""
from typing import Optional

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("*****")
        print("input:", listNodeToList(head))
        if not head:
            return None
        n = 1
        end = head
        while end.next is not None:
            end = end.next
            n += 1

        prev = None
        cur = head
        for idx in range(1, n+1):
            print(f"looking at node #{idx}", cur.val)
            if idx % 2 == 0:
                if cur.next:
                    # without this if statement you could accidentally omit the last node
                    # see test case [1, 1]
                    prev.next = cur.next
                    end.next = cur
                    end = end.next
                    cur = cur.next
                    end.next = None
            else:
                print("skipping")
                prev = cur
                cur = cur.next

        print("output", listNodeToList(head))
        return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output = Solution().oddEvenList(head)
    assert listNodeToList(output) == [1, 3, 5, 2, 4]

    head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    output = Solution().oddEvenList(head)
    assert listNodeToList(output) == [2, 3, 6, 7, 1, 5, 4]

    head = ListNode(2)
    output = Solution().oddEvenList(head)
    assert listNodeToList(output) == [2]

    output = Solution().oddEvenList(None)
    assert listNodeToList(output) == []

    head = ListNode(1, ListNode(1))
    output = Solution().oddEvenList(head)
    assert listNodeToList(output) == [1, 1]

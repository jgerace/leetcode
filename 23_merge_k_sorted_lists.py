"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""
from typing import Optional, List

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if not k:
            return None
        elif k == 1:
            return lists[0]

        def merge_lists(list1: ListNode, list2: ListNode) -> ListNode:
            node1 = list1
            node2 = list2
            dummy_head = ListNode()
            cur_output = dummy_head
            while node1 is not None or node2 is not None:
                if not node1 and node2:
                    cur_output.next = ListNode(node2.val)
                    node2 = node2.next
                    cur_output = cur_output.next
                    continue
                elif node1 and not node2:
                    cur_output.next = ListNode(node1.val)
                    node1 = node1.next
                    cur_output = cur_output.next
                    continue

                if node1.val < node2.val:
                    cur_output.next = ListNode(node1.val)
                    node1 = node1.next
                else:
                    cur_output.next = ListNode(node2.val)
                    node2 = node2.next
                cur_output = cur_output.next

            return dummy_head.next

        if k > 2:
            left_list = self.mergeKLists(lists[0: int(k/2)])
            right_list = self.mergeKLists(lists[int(k/2):])
        else:
            left_list = lists[0]
            right_list = lists[1]
        result = merge_lists(left_list, right_list)

        return result


if __name__ == "__main__":
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    output = Solution().mergeKLists(lists)
    print(listNodeToList(output))
    assert listNodeToList(output) == [1, 1, 2, 3, 4, 4, 5, 6]

    output = Solution().mergeKLists([])
    assert output is None

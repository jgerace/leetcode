"""
Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from collections import deque
from typing import List, Optional

# from testing import treeNodeToBfsList

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getList(self, root: Optional[TreeNode], inList: List[TreeNode]) -> None:
        if not root:
            return

        inList.append(root)
        self.getList(root.left, inList)
        self.getList(root.right, inList)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        treeList = list()
        self.getList(root, treeList)

        root = treeList[0]
        curPtr = root
        for node in treeList[1:]:
            curPtr.left = None
            curPtr.right = node
            curPtr = curPtr.right


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    # print(treeNodeToBfsList(tree))
    Solution().flatten(tree)
    # print(treeNodeToBfsList(tree))
    assert tree == TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))))

    Solution().flatten(None)

    tree = TreeNode(0)
    Solution().flatten(tree)
